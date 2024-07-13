def caching_fibonacci():
    """
    Outer: Creates an empty dict. Return -> inner function. 
    Inner: takes a number, checks conditions, recursively finds result. 
    Puts result into the dictionary. 
    """
    cache = {}
    def fibonacci(n):
        if n <= 0:   return 0
        elif n == 1: return 1
        elif n in cache: return cache[n]
        else: 
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]  
    return fibonacci


test_fib_func = caching_fibonacci()

print(test_fib_func(-1)) 
print(test_fib_func(0))  
print(test_fib_func(1))  
print(test_fib_func(15)) # recursion
print(test_fib_func(10)) # from cache
print(test_fib_func(15)) # from cache
print(test_fib_func(14)) # from cache
print(test_fib_func(4))  # from cache

    