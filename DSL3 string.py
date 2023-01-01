"""Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string"""

#a)To display word with the longest length
print("\nTo display word with the longest length")
str1= input("Enter the string :")
list1=str1.split()
m=0
word=0

print(list1)
for i in range(len(list1)):
    len(list1[i])
    if m<len(list1[i]):
        m=len(list1[i])
        word=i
print("The word with longeost length: ", list1[word])

#b)to determines the frequency of occurance of particular character in the string
print("\nto determines the frequency of occurance of particular character in the string")
str1=input("Enter the string :")
C=input("Entyer character :")
print("Character :",C)
g=str1.count(C)
print(g)

#To check whether given string is palindrome or not
print("\nTo check whether given string is palindrome or not")
str= input("Enter string :")
#[::-1]program has to traverse from start to end in a given list
m=str[::-1]
print(m)
if str==m:
        print("String is palindrome");
else:
        print("String not palindrome");


    
#To display index of first appearance of the substring
        
print("\nTo display index of first appearance of the substring")       
str1=input("Enter the string :")
str_sub=input("Enter substring :")
list_str = str1.split(" ")
for i in range(len(list_str)):
    if str_sub==list_str[i]:
        print(str1)
        print(i)
        break


print("\nTo count the occurrences of each word in a given string")        
str1=input("Enter the string :")
list_str=str1.split(" ")
print("********count of each word i string********")
for i in range(len(list_str)):
    print(list_str[i],list_str.count(list_str[i]))




