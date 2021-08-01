import timeit

time = timeit.timeit('"-".join(str(n) for n in range(10000))', number=10000)

print(time)