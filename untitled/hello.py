def fib(n):
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
a = fib(22)
print 'start'
print a