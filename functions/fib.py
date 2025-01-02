def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
def memo_fib(n):
    memo = {0:0, 1:1}
    
    def f(n):
        if n in memo:
            return memo[n]
        
        memo[n] = f(n-1) + f(n-2)
        return memo[n]
    
    return f(n)
