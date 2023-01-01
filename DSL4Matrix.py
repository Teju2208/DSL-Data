#Addition of two matrices
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

#Initialize matrix
matrixa = []
matrixb = []
resultmatrix=[]
print("Enter the entries rowwise:")

#For user input
for i in range(row):      # A for loop for row entries
    a =[]
    for j in range(col):   # A for loop for column entries
        a.append(int(input()))
    matrixa.append(a)

# For printing first matrix
for i in range(row):
    for j in range(col):
        print(matrixa[i][j], end = " ")
    print()
    
    
for i in range(row):
    a =[]
    for j in range(col):
        a.append(int(input()))
    matrixb.append(a)
    
    
# For printing second matrix
for i in range(row):
    for j in range(col):
        print(matrixb[i][j], end =" ")
    print()

    
# For matrix addition
for i in range(row):
    a =[]
    for j in range(col):
        
        a.append(matrixa[i][j] + matrixb[i][j])
    resultmatrix.append(a)
    
print("Addition is:")
#For printing the result matrix
for i in range(row):
    for j in range(col):
        print(resultmatrix[i][j], end =" ")
    print()








#Addition of two matrices
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

#Initialize matrix
matrixa = []
matrixb = []
resultmatrix=[]
print("Enter the entries rowwise:")

#For user input
for i in range(row):      # A for loop for row entries
    a =[]
    for j in range(col):   # A for loop for column entries
        a.append(int(input()))
        matrixa.append(a)
print(matrixa)

# For 
for i in range(row):
    for j in range(col):
        print(matrixa[i][j], end = " ")
    print()
    
    
for i in range(row):
    a =[]
    for j in range(col):
        a.append(int(input()))
    matrixb.append(a)
    
    
# For printing second matrix
for i in range(row):
    for j in range(col):
        print(matrixb[i][j], end =" ")
    print()

    
# For matrix subtraction
for i in range(row):
    a =[]
    for j in range(col):
        
        a.append(matrixa[i][j] - matrixb[i][j])
    resultmatrix.append(a)
    
    
print("Subtraction is:")
#For printing the result matrix
for i in range(row):
    for j in range(col):
        print(resultmatrix[i][j], end =" ")
    print()

#multiplication of two matrices
row1=int(input("enter the number of row:"))
col1=int(input("enter the number of columns:"))
c=0
c
#For user input
for i in range(row1):      # A for loop for row entries
    a =[]
    for j in range(col1):   # A for loop for column entries
        a.append(int(input()))
        matrixa.append(a)
print(matrixa)

print("matrix is:")
#For printing first matrix
for i in range(row1):
    for j in range(col1):
        print(matrixa[i][j], end =" ")
    print()
    
row2=int(input("enter the number of rows:"))
col2=int(input("enter the number of columns:"))

for i in range(row2):      # A for loop for row entries
    a =[]
    for j in range(col2):   # A for loop for column entries
        a.append(int(input()))
        matrixb.append(a)
        
print("matrix is:")
#For printing first matrix
for i in range(row2):
    for j in range(col2):
        print(matrixb[i][j], end =" ")
    print()
    
# For matrix addition
for i in range(row1):
    a =[]
    for j in range(col2):
        
        for k in range(row2):
            c=c+matrixa[i][j]*matrixb[k][j]
            a.append(c)
            c=0
        resultmatrix.append(a)
        
print("result martix is:")
#For printing the result matrix
for i in range(row1):
    for j in range(col2):
        print(resultmatrix[i][j], end =" ")
    print()






#Transpose of matrix
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))
a=[]
#Initialize matrix
matrixa = []
matrixb = []
result=[]

print("Enter the entries rowwise:")

#For user input
for i in range(row):      # A for loop for row entries
    a =[]
    for j in range(col):   # A for loop for column entries
        a.append(int(input()))
        matrixa.append(a)
        
# For printing second matrix
for i in range(row):
    for j in range(col):
        print(matrixb[i][j], end =" ")
    print()
    
#result matrix


for i in range(col):
    for j in range(row):
        print(resultmatrixa[i][j], end =" ")
    print()
    
    
for i in range(col):
    for j in range(row):
        print(result[i][j], end =" ")
    print()
    
#Transpose of matrix
for i in range(row):
    for j in range(col):
        result[i][j]=matrixa[i][j]

#print result 
for i in range(col):
    for j in range(row):
        print(resultmatrix[i][j], end =" ")
    print()
