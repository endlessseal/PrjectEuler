def cache_fib(x,cache = {}):
    if x in cache:
        return cache[x]
    else:
        if x > 1:
            return cache.setdefault(x, cache_fib(x-1) + cache_fib(x-2))
        else:
            return x

def is_even(x):
    if x % 2 == 0:
        return True
    return False

def solve():
    counter = 0
    value = cache_fib(counter)
    summed = 0
    while value < 4000000:
        value = cache_fib(counter)
        counter +=  1 
        if is_even(value):
            summed += value 
    print(summed)
    
solve()
