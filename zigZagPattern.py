strToZigZag=input("Enter the String need to be zigzagged: ")
countRow=int(input("Enter the number of rows needs to be taken for zig zag string :"))

column=0
while (row<len(strToZigZag)/2):
    row = 0
    while(row<countRow):
        print(strToZigZag[row][column])
        row+=1
    column+=1

