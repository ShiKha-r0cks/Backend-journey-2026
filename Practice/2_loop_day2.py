""""
topic: loops
day:2
focus:logic building
"""
# 1.count the digit in a number
num=int(input("enter the digit"))
count=0
while(num>0):
    num=num//10
    count+=1
print(count)
print("------------------------------------------------------------------")    
# 2.reverse no
no=int(input("enter the number you want to reverse"))
rev=0
digit=0
while(no>0):
    digit=no%10
    rev=rev*10+ digit
    no=no//10
print(rev)   
print("--------------------------------------------------------------------------")

# 3.sum of the digits 
SumNo=int(input("enter any no you want to sum of digits "))
sum=0
while(SumNo>0):
    rem=SumNo%10 
    sum=sum+rem
    SumNo=SumNo//10
print(sum) 
print("------------------------------------------------------------------------") 

#4. factorial of a no
Num=int(input("enter the no of which you want the factorial"))
fact=1
i=1
while(i<Num+1):
    fact=fact*i
    i+=1
print(fact)
print("-------------------------------------------------------------------------")
# 5.fibonacci series 
n=int(input("enter the no term "))
a=0
b=1
for i in range (n):
    if(a<300):
        print(a)
        a,b=b,a+b
print("--------------------------------------------------------------------")

#6.find nth fibonacci no
no1=0
no2=1
i=1
userno=int(input("enter the no "))
while(i<userno):
    no1,no2=no2,no1+no2
    i+=1
print(no1)
print("------------------------------------------------------------------------------")
#7. check prime
num=int(input("enter the a no yo want to check whther its prime or not"))
if(num<=1):
    print("not prime")
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            is_prime=False
            break
if is_prime:
    print(" prime no")
else:
    print("not prime")
print("------------------------------------------------------------------------------")

#8.pyramid
row=int(input("enter the row no"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
print("----------------------------------------------------------------------") 
#inverted pyramid
row1=int(input("enter the row no"))
for i in range(1,row1+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*(row1-i)+1):
        print("*",end="")
    print() 
       











