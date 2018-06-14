def square(num, times):
    store = 1
    for i in range(1, times + 1):
        store = store * num

    return store

k=int(input())
n=int(input())
y=square(k,n)
print(y)