import ast
import glob
import os
import re


def extract_type_hints_from_signature(signature):
    """Extracts type hints from a function signature, with improved handling of tuples and nested types."""
    pattern = r"\((.*)\)"  # Match parentheses and content within
    match = re.search(pattern, signature)
    if match:
        params = match.group(1).strip()  # Remove leading/trailing whitespace
        params = re.sub(r"\s+", "", params)  # Remove extra spaces
        params = params.split(",")
        type_hints = []
        for param in params:
            parts = param.split(":")
            if len(parts) > 1:
                type_hint = parts[1].strip()
                # Handle nested tuples recursively
                while "(" in type_hint:
                    nested_match = re.search(r"\((.*)\)", type_hint)
                    if nested_match:
                        nested_types = extract_type_hints_from_signature(nested_match.group(1))
                        type_hint = type_hint.replace(nested_match.group(0), ",".join(nested_types))
                type_hints.append(type_hint)
            else:
                type_hints.append("None")  # No type hint
        # Extract return type
        return_type_match = re.search(r"->\s*(.*)", signature)
        if return_type_match:
            return_type = return_type_match.group(1).strip()
            type_hints.append(return_type)
        return type_hints
    else:
        return []  # No signature found

def process_sor_files_with_regex(dir_path):
    """Processes SOR files, extracting function parameter types using regex, handling nested functions."""
    files = glob.glob(os.path.join("SOR9999.py"))
    for filename in files:
        try:
            with open(filename, "r") as f:
                file_content = f.read()
            function_params = {}
            # Handle nested functions by splitting on "def" while preserving indentation
            for code_block in re.split(r"(def\s+)", file_content, flags=re.M):
                for func_def in re.findall(r"^\s*def\s+(\w+)\((.*)\):", code_block, flags=re.M):
                    func_name = func_def[0]
                    param_types = extract_type_hints_from_signature(func_def[1])
                    function_params[func_name] = param_types
            print(f"{filename}: {function_params}")
        except SyntaxError:
            print(f"Error parsing {filename}: Invalid syntax")  



def check_dyn_annotation(annotation):
    if isinstance(annotation, ast.Str):
        return "Dyn" in annotation.s
    elif isinstance(annotation, ast.List):
        return any(check_dyn_annotation(elt) for elt in annotation.elts)
    elif isinstance(annotation, ast.Tuple):
        return any(check_dyn_annotation(elt) for elt in annotation.elts)
    elif isinstance(annotation, ast.Call):
        return any(check_dyn_annotation(arg) for arg in annotation.args)
    elif isinstance(annotation, ast.Attribute):
        return check_dyn_annotation(annotation.value)
    else:
        return False

def check_function_for_dyn(node):
    for arg in node.args.args:
        if arg.annotation and check_dyn_annotation(arg.annotation):
            return True
    if node.returns and check_dyn_annotation(node.returns):
        return True
    return False
def has_dyn(expr):
    """Checks if an expression contains the type 'Dyn', including nested cases
       and nested annotations within type hints."""
    if expr:
        print(expr.id)
        print(vars(expr))
    if isinstance(expr, ast.Name):
        
        return expr.id == "Dyn"
    elif isinstance(expr, (ast.Subscript, ast.Attribute)):
        return has_dyn(expr.value)
    elif isinstance(expr, (ast.Tuple, ast.List)):
        return any(has_dyn(x) for x in expr.elts)
    elif isinstance(expr, ast.NameConstant) and expr.value == "None":  # Handle NoneType
        return False
    elif isinstance(expr, ast.Subscript) and isinstance(expr.value, ast.Name) and expr.value.id == "typing":
        # Handle nested annotations within typing constructs
        return any(has_dyn(arg) for arg in expr.args)
    else:
        return False

def find_no_dyn_files(dir_path):
    """Finds all files in a directory that have no function parameters of type 'Dyn',
       filtering for files starting with the 'SOR' prefix."""
    no_dyn_files = []
    files = glob.glob(os.path.join("SOR9999.py"))
    for filename in files:
        if filename.startswith("SOR"):  # Filter for files starting with 'SOR'
            
            with open(filename, "r") as f:
                tree = ast.parse(f.read())
                has_dyn_param = False
                for func in ast.walk(tree):
                    if isinstance(func, ast.FunctionDef):
                        if check_function_for_dyn(func):
                            has_dyn_param = True
                            break
                        """for arg in func.args.args:
                            print(arg.annotation)
                            if check_function_for_dyn(arg.annotation):
                                has_dyn_param = True
                                break"""
                if not has_dyn_param:
                    no_dyn_files.append(filename)
    return no_dyn_files

# Example usage

process_sor_files_with_regex("")
"""
dir_path = os.getcwd()  # Replace with the actual directory path
no_dyn_files = find_no_dyn_files(dir_path)

if no_dyn_files:
    output_file = os.path.join(dir_path, "no_dyn_files.txt")  # Customize output filename
    with open(output_file, "w") as f:
        for filename in no_dyn_files:
            f.write(filename + "\n")
    print("Total: ",len(no_dyn_files))
    print("Files with no function parameters of type 'Dyn':")
    #for filename in no_dyn_files:
    #    print(filename)
else:
    print("No files found with no function parameters of type 'Dyn'.")
"""