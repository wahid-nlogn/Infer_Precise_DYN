import random
header = """from array import array
import math

from six.moves import xrange
import time

#Assign the function array2d the type: Function(['w:Dyn', 'h:Dyn', 'data:Dyn'], Tuple(Dyn,Dyn,Dyn))
#Assign the function idx the type: Function(['arr:Tuple(Int,Int,Dyn)', 'x:Int', 'y:Choice c<Dyn, Int>'], Int)
#Assign the function getitem the type: Function(['arr:Tuple(Dyn,Dyn,Dyn)', 'x_y:Tuple(Int,Choice c<Dyn, Int>)'], Dyn)
#Assign the function setitem the type: Function(['arr:Tuple(Int,Int,Dyn)', 'x_y:Tuple(Int,Choice c<Dyn, Int>)', 'val:Dyn'], Tuple(Dyn,Dyn,Dyn))
#Assign the function SOR_execute the type: Function(['omega:Choice o<Dyn, Float>', 'G:Tuple(Dyn,Dyn,Choice f<Dyn, Float>)', 'cycles:Choice q<Dyn, Int>'], Void)
#Assign the function bench_SOR the type: Function(['loops:Choice g<Dyn, Int>', 'n:Dyn', 'cycles:Int'], Void)
#Assign the function main the type: Function([], Void)

#def array2d(w, h):
def array2d(w, h)->Tuple(Dyn,Dyn,Dyn):
    d = array('d', [0.0]) * (w * h)
    #if data is not None:
    #    return setup(d,data)
    return (w, h, d)

"""

idx_headers = ["def idx(arr:Tuple(Dyn, Dyn, Dyn), x, y):",
    "def idx(arr, x, y) -> int:",
    "def idx(arr:Dyn, x, y) -> int:",
    "def idx(arr, x:int, y:int) -> int:",
    "def idx(arr:Tuple(int,int,Dyn), x ,  y)->int:",
    "def idx(arr:Tuple(int,int,Dyn), x : int,  y:int)->int:"
]
idx_body = """
    w,h,d = arr
    if 0 <= x < (w+0) and 0 <= y < (h+0):
        return (y+0) * (w+0)  + x + 0
    raise IndexError
    return 0

"""
getitem_headers = [
    "def getitem(arr:Tuple(Dyn,Dyn,Dyn), x_y):",
    "def getitem(arr, x_y:Tuple(Dyn,Dyn)):",
    "def getitem(arr, x_y:Tuple(int,Dyn)):",
    "def getitem(arr:Tuple(Dyn,Dyn,Dyn), x_y:Tuple(int,Dyn)):",
    "def getitem(arr, x_y:Tuple(Dyn,int)):",
    "def getitem(arr:Tuple(Dyn,Dyn,Dyn), x_y:Tuple(Dyn,int)):",
    "def getitem(arr:Tuple(int,int,Dyn), x_y:Tuple(int,int)): "
]
getitem_body = """
    w,h,d = arr
    (x, y) = x_y
    return d[idx(arr, x, y)]

"""

setitem_headers = [
    "def setitem(arr:Tuple(Dyn, Dyn, Dyn), x_y:Tuple(Dyn, Dyn), val)->Tuple(Dyn,Dyn,Dyn):",
    "def setitem(arr:Tuple(int,int,Dyn), x_y, val)->Tuple(Dyn,Dyn,Dyn):",
    "def setitem(arr, x_y:Tuple(int,int), val)->Tuple(Dyn,Dyn,Dyn):",
    "def setitem(arr:Tuple(int,int,Dyn), x_y:Tuple(int,int), val)->Tuple(Dyn,Dyn,Dyn):   ",
    "def setitem(arr, x_y, val:float)->Tuple(Dyn,Dyn,Dyn):   ",
    "def setitem(arr, x_y:Tuple(int,int), val:float)->Tuple(Dyn,Dyn,Dyn):   ",
    "def setitem(arr:Tuple(int,int,Dyn), x_y, val:float)->Tuple(Dyn,Dyn,Dyn):   ",
    "def setitem(arr:Tuple(int,int,Dyn), x_y:Tuple(int,int), val:float)->Tuple(Dyn,Dyn,Dyn):   "
    ]
setitem_body = """
    (x, y) = x_y
    w, h, d = arr
    d[idx(arr, x, y)] = val
    return (w, h, d)

"""

SOR_execute_headers = [
    "def SOR_execute(omega, G:Tuple(Dyn, Dyn, Dyn), cycles):",
    "def SOR_execute(omega:float, G, cycles):",
    "def SOR_execute(omega, G:Tuple(int,int,Dyn), cycles):",
    "def SOR_execute(omega, G, cycles:int):",
    "def SOR_execute(omega:float, G:Tuple(int,int,Dyn), cycles):",
    "def SOR_execute(omega:float, G, cycles:int):",
    "def SOR_execute(omega, G:Tuple(int,int,Dyn), cycles:int):",
    "def SOR_execute(omega:float, G:Tuple(int,int,Dyn), cycles:int):"]
SOR_execute_body = """
    w,h,d = G
    for p in xrange(cycles+0):
        for y in xrange(1, h - 1):
            for x in xrange(1, w - 1):
                G = setitem(G,(x, y), (omega * 0.25 * (getitem(G,(x, y - 1)) + getitem(G,(x, y + 1)) + getitem(G,(x - 1, y))
                                                     + getitem(G,(x + 1, y))))
                           + (1.0 - omega) * getitem(G,(x, y)))
    return None

"""
bench_SOR_headers = [
    "def bench_SOR(loops, n, cycles):",
    "def bench_SOR(loops:int, n, cycles):",
    "def bench_SOR(loops, n:int, cycles):",
    "def bench_SOR(loops, n, cycles:int):",
    "def bench_SOR(loops:int, n:int, cycles):",
    "def bench_SOR(loops:int, n, cycles:int):",
    "def bench_SOR(loops, n:int, cycles:int):",
    "def bench_SOR(loops:int, n:int, cycles:int):"]
bench_SOR_body = """
    range_it = xrange(loops+0)
    t0 = time.time()#perf.perf_counter()

    for _ in range_it:
        G = array2d(n, n)
        SOR_execute(1.25, G, cycles+0)#, Array)
    t1 = time.time()
    print(t1 - t0)
    return None
    #return t1 - t0#perf.perf_counter() - t0

"""
rest = """

def main():
    bench_SOR(4,10,1)

main()

"""

indexList = []
"""
i = 1
while i <= 1024:

    idx_index = random.randrange(0, len(idx_headers))
    getitem_index = random.randrange(0, len(getitem_headers))
    setitem_index = random.randrange(0,len(setitem_headers))
    SOR_execute_index = random.randrange(0, len(SOR_execute_headers))
    bench_SOR_index = random.randrange(0, len(bench_SOR_headers))

    if not (idx_index, getitem_index, setitem_index, SOR_execute_index, bench_SOR_index) in indexList:
        indexList.append((idx_index, getitem_index, setitem_index, SOR_execute_index, bench_SOR_index))
        i += 1
        idx = idx_headers[idx_index]  + idx_body
        getitem = getitem_headers[getitem_index]  + getitem_body
        setitem = setitem_headers[setitem_index]  + setitem_body
        SOR_execute = SOR_execute_headers[SOR_execute_index]  + SOR_execute_body
        bench_SOR = bench_SOR_headers[bench_SOR_index]  + bench_SOR_body

        program = header +  idx + getitem + setitem + SOR_execute + bench_SOR + rest
        programName = "SOR" + str(i) + ".py"
        with open(programName, 'w+') as f:
            f.write(program)
"""

if __name__ == "__main__":
    i = 0
    for idx_ann in idx_headers:
        for getitem_ann in getitem_headers:
            for setitem_ann in setitem_headers:
                for SOR_execute_ann in SOR_execute_headers:
                    for bench_SOR_ann in bench_SOR_headers:
                        idx = idx_ann + idx_body
                        getitem = getitem_ann + getitem_body
                        setitem = setitem_ann + setitem_body
                        SOR_execute = SOR_execute_ann + SOR_execute_body
                        bench_SOR = bench_SOR_ann + bench_SOR_body
                        program = header +  idx + getitem + setitem + SOR_execute + bench_SOR + rest
                        i += 1
                        programName = "SOR" + str(i) + ".py"
                        with open(programName, 'w+') as f:
                            f.write(program)
