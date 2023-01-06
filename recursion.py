def count(n):
    if n ==1:
        return 1
    return n+count(n-1)

print(count(10))