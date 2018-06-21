def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    l = []
    '''This for loop is used to store 1 on every position of a pascal triangle'''
    for i in range(numRows):
        under = []
        count = 0
        for x in range(i + 1):
            under.append(1)
        l.append(under)
    '''This for loop is used to add the element of a row and store it on particular index of a columm of next row
        that comes in between the index of these column'''
    for z in range(numRows):
        for x in range(z + 1):
            sum = 0
            if z != numRows - 1:
                if x > 0:
                    if x <= z + 1:
                        sum = l[z][x] + l[z][x - 1] # Adding the values of these columns if the columns are greater than one
                        l[z + 1][x] = sum           # storing this value on a column index of a next row
    return l # returning the updates Pascal Triangle List

numRows=int(input("Enter the Number of rows need to be inserted in Triangle : "))
k=generate(numRows)# passing rows to the function generate
print(k)