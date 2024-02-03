import random
from functools import reduce
start = """
import time
"""
 
pascal_upp_headers = ["def pascal_upp(n):", "def pascal_upp(n:Int):", "def pascal_upp(n:Int) -> List(List(Int)):","def pascal_upp(n:Dyn) -> List(List(Dyn)):",
"def pascal_upp(n:Dyn) -> List(Dyn):"]
pascal_upp_body = """
    s = [[0  for _ in range(n)] for _ in range(n)]
    s[0] = [1  for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            s[i][j] = s[i-1][j-1] + s[i][j-1]
    return s
"""
 
pascal_low_headers = ["def pascal_low(n):", "def pascal_low(n:Int):", "def pascal_low(n:Int) -> List(List(Int)):","def pascal_low(n:Dyn) -> List(List(Dyn)):",
"def pascal_low(n:Dyn) -> List(Dyn):"]
pascal_low_body = """
    # transpose of pascal_upp(n)    
    return [list(x) for x in zip(*pascal_upp(n))]
"""
 
pascal_sym_headers = ["def pascal_sym(n):", "def pascal_sym(n:Int):", "def pascal_sym(n:Int) -> List(List(Int)):","def pascal_sym(n:Dyn) -> List(List(Dyn)):",
"def pascal_sym(n:Dyn) -> List(Dyn):"]
pascal_sym_body = """
    s = [[1  for _ in range(n)] for _ in range(n)] 
    for i in range(1, n):
        for j in range(1, n):
            s[i][j] = s[i-1][j] + s[i][j-1]
    return s
"""

printMatrix_headers = ["def printMatrix(matrix):", "def printMatrix(matrix:List(List(Int))):","def printMatrix(matrix:List(List(Dyn))):","def printMatrix(matrix:List(Dyn)):"]
printMatrix_body = """
    #print(string)
    #pp(m)
    return
"""

printMatrixes_headers = ["def printMatrixes(n):", "def printMatrixes(n:Int):"]
printMatrixes_body = """
    #print("\\nUpper:")
    printMatrix(pascal_upp(n))
    #print("\\nLower:")
    printMatrix(pascal_low(n))
    #print("\\nSymmetric:")
    printMatrix(pascal_sym(n))
"""

nextperm_headers = ["def nextperm(a):", "def nextperm(a:List(Int))->Bool:","def nextperm(a:List(Dyn))->Dyn:"]
nextperm_body = """
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] > a[i]:
        i -= 1
    j = i
    k = n - 1
    while j < k:
        a[j], a[k] = a[k], a[j]
        j += 1
        k -= 1
    if i == 0:
        return False
    else:
        j = i
        while a[j] < a[i - 1]:
            j += 1
        a[i - 1], a[j] = a[j], a[i - 1]
        return True
"""
 
perm3_headers = ["def perm3(n:Int, flag):", "def perm3(n, flag:Bool):", "def perm3(n:Int, flag:Bool) -> List(Dyn):"]
perm3_body = """
    if (flag):
        if (n < 1):
            return []
        z = range(n)
    else:
        z = sorted(n)
    a = list(z)
    u = [list(a)]
    while nextperm(a):
        u.append(list(a))   
    return u
"""

main_headers = ["def main(x, y, z):",
                "def main(x:Int, y, z:Bool):",
                "def main(x, y:Int, z):",
                "def main(x, y, z:Bool):",
                "def main(x:Int, y:Int, z):",
                "def main(x:Int, y, z:Bool):",
                "def main(x, y:Int, z:Bool):",
                "def main(x:Int, y:Int, z:Bool):",
                "def main(x:Dyn, y:Dyn, z:Dyn):"]
main_body = """
        for p in perm3(x, z):
            break
        for i in range(1000):
            printMatrixes(y)
"""
rest = """
t0 = time.time()
main(3, 3, True)
t1 = time.time()
print(t1-t0)
"""
def random_element(collection):
    return collection[random.randrange(0, len(collection))]
i = 0
name = "pascal"

for pascal_upp_header in pascal_upp_headers:
    
    for pascal_low_header in pascal_low_headers:
        
        for pascal_sym_header in pascal_sym_headers:
           
            for printMatrix_header in printMatrix_headers:
               
                for printMatrixes_header in printMatrixes_headers:
                   
                    for nextperm_header in nextperm_headers:
                        
                        for perm3_header in perm3_headers:
                            
                            for main_header in main_headers:
                               
                                pascal_upp = pascal_upp_header +pascal_upp_body
                                pascal_low = pascal_low_header + pascal_low_body
                                pascal_sym = pascal_sym_header+ pascal_sym_body
                                printMatrix =  printMatrix_header + printMatrix_body
                                printMatrixes = printMatrixes_header+printMatrixes_body
                                nextperm = nextperm_header+nextperm_body
                                perm3 = perm3_header + perm3_body
                                main = main_header + main_body
                                prog = reduce(lambda x, y: x+y, [start,
                                                                pascal_upp,
                                                                pascal_low,
                                                                pascal_sym,
                                                                printMatrix,
                                                                printMatrixes,
                                                                nextperm,
                                                                perm3,
                                                                main,
                                                                rest], "")
                                i+=1
                                with open(name + str(i) + ".py", 'w+') as f:
                                    f.write(prog)

print(i, 'files generated')
