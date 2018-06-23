'''You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.'''
def climbStairs(n):
# This is a problem of a fibonacci number where the number of distinct steps is this case are the sum of the number of possibilities of preceding steps
    current=1
    preceding=0
    storetemp=0
    for i in range(n):
        storetemp=current # storing the current position to a temporary variable in order to add it get the next step
        current=current+preceding # current is changed to new current by adding the preding values
        preceding=storetemp # storing the temp value to preceding in order to maintain track of preceding and current value
    return current
k=int(input())
result=climbStairs(k)
print(result)