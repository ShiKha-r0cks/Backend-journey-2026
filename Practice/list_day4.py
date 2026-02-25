# topic list ,set,tuples
# day4

#Take 5 numbers from user → store in list → print sum
list=[]
sum=0
for i in range(5):
     num= int(input("enter the value"))
     list.append(num)
     sum+=num
print(sum)

#Find max and min manually (without using max())
Number=[]

while True:
     num=int(input("enter no"))
     Number.append(num)
     term=input("do you want to continue:yes/no")
     if term.strip().lower()!='yes':
          break

max=Number[0]
min=Number[0]
total=0

for i in Number:
     if(max<i):
          max=i
     if(min>i):
          min=i
     total+=i
avg=total/len(Number)
print(max,min,avg)
