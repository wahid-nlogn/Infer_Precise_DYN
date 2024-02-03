from array import array
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

def idx(arr, x:int, y:int) -> int:
    w,h,d = arr
    if 0 <= x < (w+0) and 0 <= y < (h+0):
        return (y+0) * (w+0)  + x + 0
    raise IndexError
    return 0

def getitem(arr, x_y:Tuple(Dyn,Dyn)):
    w,h,d = arr
    (x, y) = x_y
    return d[idx(arr, x, y)]

def setitem(arr:Tuple(int,int,Dyn), x_y, val:float)->Tuple(Dyn,Dyn,Dyn):   
    (x, y) = x_y
    w, h, d = arr
    d[idx(arr, x, y)] = val
    return (w, h, d)

def SOR_execute(omega, G:Tuple(int,int,Dyn), cycles):
    w,h,d = G
    for p in xrange(cycles+0):
        for y in xrange(1, h - 1):
            for x in xrange(1, w - 1):
                G = setitem(G,(x, y), (omega * 0.25 * (getitem(G,(x, y - 1)) + getitem(G,(x, y + 1)) + getitem(G,(x - 1, y))
                                                     + getitem(G,(x + 1, y))))
                           + (1.0 - omega) * getitem(G,(x, y)))
    return None

def bench_SOR(loops:int, n:int, cycles:int):
    range_it = xrange(loops+0)
    t0 = time.time()#perf.perf_counter()

    for _ in range_it:
        G = array2d(n, n)
        SOR_execute(1.25, G, cycles+0)#, Array)
    t1 = time.time()
    print(t1 - t0)
    return None
    #return t1 - t0#perf.perf_counter() - t0



def main():
    bench_SOR(4,10,1)

main()

