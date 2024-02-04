import glob
import re
import os
import ast
def extract_function_parameter_hints(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find function definitions
    function_defs = re.findall(r'def\s+(\w+)\s*\(([^)]*)\)', content)

    parameter_hints = {}
    for function_name, param_list in function_defs:
        # Use regular expression to extract parameter hints with nested tuples
        hints = re.findall(r'(\w+)\s*:\s*(\w+(?:\([^)]*\)(?:,\s*\w+\([^)]*\))*)?)', param_list)

        # Format the hints into 'param:Type(...)' if there are nested tuples
        formatted_hints = [f"{param}:{Type}" if '(' in Type else f"{param}:{Type}" for param, Type in hints]

        parameter_hints[function_name] = formatted_hints

    return parameter_hints

def extract_function_parameter_hints_with_regex(file_path):
    """Extracts function parameter hints using refined regular expressions."""
    function_hints = {}
    with open(file_path, "r") as f:
        file_content = f.read()

        def_pattern = r"def\s+(\w+)\((.*?)\):"
        param_pattern = r"(\w+(?:\:\s*\w+)?)(,\s*)?"  # Capture type and optional name

        for match in re.finditer(def_pattern, file_content, re.DOTALL):
           
            
            function_name = match.group(1)
            param_hints = [
                hint.group(1).strip()
                for hint in re.finditer(param_pattern, match.group(2))
            ]
            function_hints[function_name] = param_hints

    return function_hints

def process_sor_files():
    """Processes SOR files in the current directory, extracting function hints."""
    files = glob.glob(os.path.join("SOR9999.py"))
    for filename in files:
        hints = extract_function_parameter_hints_with_regex(filename)
        print(f"{filename}: {hints}")

if __name__ == "__main__":
    process_sor_files()

