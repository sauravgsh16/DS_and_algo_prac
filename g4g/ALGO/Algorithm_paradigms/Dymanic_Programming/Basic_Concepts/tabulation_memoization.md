# TABULATION AND MEMOIZATION

Two patterns to solve DP
1) `Tabulation` -- Bottom Up
2) `Memoization` -- Top Down

### Tabluation or Bottom up

This is the process where we start from the bottom state and calculate the
final result.

```py
# Calculation nth fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    mem[i] = [0] * n+1
    mem[1] = 1
    mem[2] = 1
    for i in range(3, n+1):
        mem[i] = m[i-1] + mem[i-2]
    return mem[n]
```

### Memoization or Top Down

Here we start our journey from the top most destination state and compute its
answer by taking into account the values of states that can reach the 
destination state, till we reach the bottom most `base state`

They may be instances where we calculate the same result over and over.
To avoid this, we store the result of the `call`, so that next time we
encounter the `same call`, we can retreive the value from the `cache`

```py
def fib(n):
    if n == 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
```


