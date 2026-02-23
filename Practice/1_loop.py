# day 1 loop parctice
# starting on 21 feb 2026


#print number from 1 to 20
i=1
while (i<21):
      print(i)
      i=i+1   
print("------------------------")
#print number from 1 to 51 which are even
i=1
while(i<51):
      if(i%2==0):
            print(i)
      i=i+1
print("-------------------------")
# table of 7
i=1
while(i<11):
      print(7*i)
      i=i+1
print("-----------------------------")
#sum of no from 1 to 100
i=1
sum=0 
while(i<101):
      sum+=i
      i=i+1
print(sum)
print("-----------------------------------")

# print this pattern
#    *
#    **
#    *** 
#    **** 
#    *****
i=1

while i<6:
      j=1
      while(j<=i):
            print("*",end="")
            j=j+1
      print()
      i=i+1      
print("-------------------")   

# take a no from user and print whether its prime or not
no=int(input("enter a no "))
count=0
for i in range(1,no+1):
      if (no%i==0):
            count+=1
print(count)      
if(count==2):
      print("its a prime no")
else:
      print("its not prime") 

