from retic.runtime import *
from retic.guarded import *
from retic.typing import *
from array import array
import math
from six.moves import xrange
import time

def array2d(w, h):
    d = (retic_cast(array, Dyn, Function(AnonymousParameters([String, List(Float)]), Dyn), "\nSOR1000.py:17:8: Expected function of type Function(['String', 'List(Float)'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")('d', [0.0]) * (w * h))
    return (w, h, d)

def idx(arr, x, y):
    (w, h, d) = arr
    if ((0 <= x < (w + 0)) and (0 <= y < (h + 0))):
        return ((((y + 0) * (w + 0)) + x) + 0)
    raise IndexError
    return retic_cast(0, Int, Dyn, '\nSOR1000.py:27:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def getitem(arr, x_y):
    (w, h, d) = retic_cast(arr, Dyn, Tuple(Dyn, Dyn, Dyn), '\nSOR1000.py:30:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    (x, y) = x_y
    return d[idx(retic_cast(arr, Dyn, Tuple(Dyn, Dyn, Dyn), '\nSOR1000.py:32:13: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), x, y)]

def setitem(arr, x_y, val):
    (x, y) = x_y
    (w, h, d) = arr
    d[idx(retic_cast(arr, Tuple(Int, Int, Dyn), Tuple(Dyn, Dyn, Dyn), '\nSOR1000.py:37:6: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast(x, Int, Dyn, '\nSOR1000.py:37:6: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(y, Int, Dyn, '\nSOR1000.py:37:6: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))] = retic_cast(val, Float, Dyn, '\nSOR1000.py:37:4: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    return retic_cast((w, h, d), Tuple(Int, Int, Dyn), Tuple(Dyn, Dyn, Dyn), '\nSOR1000.py:38:4: A return value of type Tuple(Dyn,Dyn,Dyn) was expected but a value %s was returned instead. (code RETURN_ERROR)')

def SOR_execute(omega, G, cycles):
    (w, h, d) = G
    for p in retic_cast(xrange, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nSOR1000.py:42:13: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((cycles + 0)):
        for y in retic_cast(xrange, Dyn, Function(AnonymousParameters([Int, Int]), Dyn), "\nSOR1000.py:43:17: Expected function of type Function(['Int', 'Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(1, (h - 1)):
            for x in retic_cast(xrange, Dyn, Function(AnonymousParameters([Int, Int]), Dyn), "\nSOR1000.py:44:21: Expected function of type Function(['Int', 'Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(1, (w - 1)):
                G = retic_cast(setitem(G, retic_cast((x, y), Tuple(Dyn, Dyn), Tuple(Int, Int), '\nSOR1000.py:45:20: Expected argument of type Tuple(Int,Int) but value %s was provided instead. (code ARG_ERROR)'), retic_cast((((omega * 0.25) * (((getitem(retic_cast(G, Tuple(Int, Int, Dyn), Dyn, '\nSOR1000.py:45:55: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), (x, (y - 1))) + getitem(retic_cast(G, Tuple(Int, Int, Dyn), Dyn, '\nSOR1000.py:45:79: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), (x, (y + 1)))) + getitem(retic_cast(G, Tuple(Int, Int, Dyn), Dyn, '\nSOR1000.py:45:103: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), ((x - 1), y))) + getitem(retic_cast(G, Tuple(Int, Int, Dyn), Dyn, '\nSOR1000.py:46:55: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), ((x + 1), y)))) + ((1.0 - omega) * getitem(retic_cast(G, Tuple(Int, Int, Dyn), Dyn, '\nSOR1000.py:47:45: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), (x, y)))), Dyn, Float, '\nSOR1000.py:45:20: Expected argument of type Float but value %s was provided instead. (code ARG_ERROR)')), Tuple(Dyn, Dyn, Dyn), Tuple(Int, Int, Dyn), '\nSOR1000.py:45:16: Right hand side of assignment was expected to be of type Tuple(Int,Int,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    return retic_cast(None, Void, Dyn, '\nSOR1000.py:48:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def bench_SOR(loops, n, cycles):
    range_it = retic_cast(xrange, Dyn, Function(AnonymousParameters([Int]), Dyn), "\nSOR1000.py:51:15: Expected function of type Function(['Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((loops + 0))
    t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nSOR1000.py:52:9: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nSOR1000.py:52:9: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
    for _ in range_it:
        G = array2d(retic_cast(n, Int, Dyn, '\nSOR1000.py:55:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(n, Int, Dyn, '\nSOR1000.py:55:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
        SOR_execute(1.25, retic_cast(G, Tuple(Dyn, Dyn, Dyn), Tuple(Int, Int, Dyn), '\nSOR1000.py:56:8: Expected argument of type Tuple(Int,Int,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast((cycles + 0), Int, Dyn, '\nSOR1000.py:56:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nSOR1000.py:57:9: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nSOR1000.py:57:9: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
    retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nSOR1000.py:58:4: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
    return retic_cast(None, Void, Dyn, '\nSOR1000.py:59:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def main():
    bench_SOR(4, 10, 1)
main()
