
def sort(prices):
  if not prices:
      return 0
    arr.sort()
    profit = arr[-1] - arr[0]
    return profit


arr=[]
for i in range(1,6):
    arr.append(int(input("Enter the %d price : "%i)))

k=sort(arr)
print(k)
