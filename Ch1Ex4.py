# Write a generator that alternates between returning Even and Odd
def NumAlternate():
    while True:
        yield "Even"
        yield "Odd"

n = NumAlternate()

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))