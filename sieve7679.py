
import time

class Stream:
    first = None
    rest = None
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
#--------------------------------------------------------------------------------------------------
def stream_first(st:Stream) -> Int:
    return st.first
def stream_rest(st:Stream):
    return st.rest
def make_stream (hd:Int, thunk:Function([],Stream))->Stream:
    return Stream(hd, thunk)
def stream_unfold(st:Stream)-> Tuple(Int,Stream):
    return (stream_first(st), stream_rest(st)())
def stream_get(st:Stream, i:Int)->Int:
    (hd, tl) = stream_unfold(st)
    return (hd if i == 0 else stream_get(tl, i-1))
def stream_take(st:Stream, n:Int) -> List(Int):
     if n == 0:
         return []
     else:
         (hd, tl) = stream_unfold(st)
         return [hd] + stream_take(tl, n-1)
def count_from(n:Int) -> Stream:
  return make_stream(n, lambda: count_from(n+1))
def sift(n:Int, st:Stream):
    (hd, tl) = stream_unfold(st)
    return (sift(n, tl) if hd % n == 0 else make_stream(hd, (lambda: sift(n, tl))))
def sieve(st:Stream) -> Stream:
    (hd, tl) = stream_unfold(st)
    return make_stream(hd, (lambda: sieve(sift(hd, tl))))

# stream of prime numbers
#(: primes stream)
def primes():
    return sieve(count_from(2))

# Compute the 10,000th prime number
#(: N-1 Natural)
N_1 = 9

#(: main (-> Void))
def main():
  stream_get(primes(), N_1)

t0 = time.time()
for i in range(10):
    main()
t1 = time.time()
print(t1-t0)
            
#(time (main))
