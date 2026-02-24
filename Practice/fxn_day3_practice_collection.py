# function practice
#day-4
# goal - create a cli 

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact
def fibonac(n):
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,b+a
    return result

def prime(n):
    if(n<=1):
        return " not prime"
    
        
    for i in range(2,int(n**0.5)+1):
         if(n%i==0):
             return "Not prime"
                
    return "prime"

def reverse(n):
    rev=0
    digit=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev

def sum_of_digit(n):
    sum1=0
    while(n>0):
        mod=n%10
        sum1+=mod
        n=n//10
    return sum1

# creating menu for user so that the select which program they want


while True:
    print("choose program\n 1.factorial \n 2.fibonaaci no \n 3.prime no \n 4.reverse no \n 5.sum of digits")

    choice=int(input( "enter the choice"))
    n=int(input("enter the no"))
    if choice==1:
        print(factorial(n))
    elif choice==2:
        print(fibonac(n))
    elif choice==3:
        print(prime(n))
    elif choice==4:
        print(reverse(n))
    elif choice==5:
        print(sum_of_digit(n))
    else :
        print("invalid")

    again=input("enter do you want try again: yes/no")
    if again.strip().lower()!= "yes":
        break