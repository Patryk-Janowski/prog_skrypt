def g1(x):
    for n in range(x):
        yield n**2

gen = g1(100)


print(iter(gen))
print(*gen)