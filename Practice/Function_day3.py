# topic-Function
# day-3
# goal-logic building and make code no redundant

# Factorial using function 
def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    print(fact)    
num=int(input("enter the number of which you want the factorial "))
factorial(num)
# to check is_prime
def prime(n):
    if(n<=1):
        print("not prime")
    else:
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                is_prime=False
                break
    if is_prime:
        print("prime no")
    else:
        print("not prime")
n=int(input("enter the for which you want check prime :" ))
prime(n)
# Fibonacci no using function
def fibonac(no):
    a=0
    b=1
    for i in range(no):
        print(a)
        a,b=b,b+a
n0=int(input("enter the no of term:"))
fibonac(n0)
# Reverse the number 
def rev(num1):
    reverse=0
    while(num1>0):
        last_digit=num1%10
        reverse=reverse*10+last_digit
        num1=num1//10
    print(reverse)
num1=int(input("enter the no you want to reverse"))
rev(num1) 
# sum of digit
def sum_of_digit(n1):
    sum=0
    while(n1>0):
        sum+=n1%10
        n1=n1//10
    return sum
n1=int(input("enter the no to calculate the sum of digit" ))
print(sum_of_digit(n1))




        
        
        
