#  recursion in python


def factorial(n):
    if(n==0 or n==1):
        return 1 
    else :
        return n * factorial(n-1)  # recursive call
    
    
# Example 
print("Factorial of 5 is:", factorial(5))   



# fibonacci series using recursion

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive call        
    
# Example
print("Fibonacci series up to 10 terms:")
for i in range(10):
    print(f"fibonacci if {i}",{fibonacci(i)})  