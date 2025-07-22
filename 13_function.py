def cal(a,b):
    val = a+b
    print("sum is a and b is - ",val)
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
    
    
x = 4
y = 5

cal(x,y)   
    
# default arguments in def funtion

def multiply(x = 2, y= 3):
    print("multi of x and y is - ", x *y)

multiply(3,5)
multiply()
multiply(4)
multiply(y=7)
multiply(y=7,x=5)

# number tuple - group of number
def avg(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum+i
    return sum/len(num)
        
print(avg(3,4,5,6,7,8))