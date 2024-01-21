
import time
def pascal_upp(n:Dyn) -> List(List(Dyn)):
    s = [[0  for _ in range(n)] for _ in range(n)]
    s[0] = [1  for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            s[i][j] = s[i-1][j-1] + s[i][j-1]
    return s
def pascal_low(n:Dyn) -> List(List(Dyn)):
    # transpose of pascal_upp(n)    
    return [list(x) for x in zip(*pascal_upp(n))]
def pascal_sym(n:Dyn) -> List(List(Dyn)):
    s = [[1  for _ in range(n)] for _ in range(n)] 
    for i in range(1, n):
        for j in range(1, n):
            s[i][j] = s[i-1][j] + s[i][j-1]
    return s
def printMatrix(matrix:List(List(Dyn))):
    #print(string)
    #pp(m)
    return
def printMatrixes(n:Dyn):
    #print("\nUpper:")
    printMatrix(pascal_upp(n))
    #print("\nLower:")
    printMatrix(pascal_low(n))
    #print("\nSymmetric:")
    printMatrix(pascal_sym(n))
def nextperm(a:List(Dyn))->Dyn:
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
def perm3(n:Dyn, flag:Dyn) -> List(Dyn):
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
def main(x:Dyn, y:Dyn, z:Dyn):
        for p in perm3(x, z):
            break
        for i in range(1000):
            printMatrixes(y)

t0 = time.time()
main(3, 3, True)
t1 = time.time()
print(t1-t0)
