def countPrimes(number):
    if number < 2: # checking if number is less than 2 returning 0 since there are no prime number under 2
        return 0
    storeTemp = [1] * number # defined list of size n and assigned every element to 1
    storeTemp[0] = storeTemp[1] = 0 # assigned 0 to first and second element since they are 0 and 1 and they are not prime numbers
    for i in range(2, int(number ** 0.5) + 1): # we are running for loop from 2nd element till the square root of n plus one number
        if storeTemp[i] == 1: # if s[i] is 1 then
            storeTemp[i * i:number:i] = [0] * int((number - i * i - 1) / i + 1) # assign 0 to  every number multiple of i since that every multiple number is already divisible by i
    return sum(storeTemp) # returning the sum of 1`s left in list s since they are the prime numbers left


k=int(input("Enter the number you want to find prime for : "))
result=countPrimes(k)
print(result)