def fibonacci(num):
    cache = {}

    def recursion(n):
        if n in cache:
            return cache[n]

        if n < 2:
            cache[n] = n
            return n

        cache[n] = recursion(n-1) + recursion(n-2)
        return cache[n]

    recursion(num)

    return cache[num]


result = fibonacci(5)
print(result)