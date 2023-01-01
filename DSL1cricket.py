"""In second year computer engineering class, group A student’s play cricket,
group B students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions) """

groupA=['Aman','Raj','Atharva', 'Ruchi'] 
groupB=['Aman','Saloni','Aditya','Ayush','Atharva']
groupC=['Raj','Ruchi','Vedant','Atharva']

lena=len(groupA)
lenb=len(groupB)

#List of students who play both cricket and badminton 
print("1.List of students who play both cricket and badminton");
resultlistCB=[];
for i in range(lenb):
    for var in range(lena):
      if (groupB[i]==groupA[var]):
          resultlistCB.append(groupB[i]);
          break;
print(resultlistCB)    
       
#list of students who play either cricket or badminton but not both
print("2.list of students who play either cricket or badminton but not botoh")
resultlistCBN=[];
flag=0;

for i in range(lenb):
    for var in range(lena):
        if(groupB[i]==groupA[var]):
            flag=1;
    if(flag==0):
        resultlistCBN.append(groupB[i]);
    flag=0;        
else:
     for i in range(lena):
        for var in range(lenb):
            if(groupA[i]==groupB[var]):
                flag=1;
        if(flag==0):
            resultlistCBN.append(groupA[i]);
        flag=0;        
print(resultlistCBN)


#vedant

print("3.Number of students who play nither cricket not badminton");
resultlistNF=[];

lenc=len(groupC)
for i in range(lenc):
    for var in range(lenb):
       if(groupB[var]==groupC[i]):
          flag=1;
          break;
    for var1 in range(lena):
       if(groupA[var1]==groupC[i]):
           flag=1;
    if(flag==0):
        resultlistNF.append(groupC[i]);
    flag=0;
print(resultlistNF)    

print("4.Number of students who play cricket and football but not badminton.");

print("A.Number of students who play ckicket")
groupckt=[]
for i in range(lena):
    groupckt.append(groupA[i]);
print(groupckt)

print("B.Number of studenr who play football")
groupft=[];
for var in range(lenc):
    groupft.append(groupC[var]);
print(groupft)
                            
"""groupA=['Aman','Raj','Atharva', 'Ruchi']                
groupC=['Raj','Ruchi','Vedant','Atharva']"""
 


        
