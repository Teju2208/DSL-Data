"""Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following: D
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500"""



def deposit(num):
    global balance                 # balance 0 300 - num  balance+=1 balance= balance+num
    balance=balance+num 
def withdrawal(num):                #balance 300 100-num   balance = balance - num / 99  - 100 wrong case
    global balance
    if(balance>num):
        balance=balance-num
    else:
        print("Withdraw not possible because balance is less.")
    

list1=[] 
balance=0
while True:
    '''While loop is used to execute a block of code repeatedly until given boolean condition
    evaluated to False.If we write while True then the loop will run forever.'''
    
    data=input("Please enter the tranaction details:\n")
    if 'Exit'== data:
        break
    list1.append(data.split())
print(list1)

for var in list1:
    if(var[0]=='D'):      
        deposit(int(var[1]))
    elif(var[0]=='W'):
        withdrawal(int(var[1]))
print("Balance is:",balance)
