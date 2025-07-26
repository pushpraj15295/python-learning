# string formating 

s = "Hello, {}. Today is {}."
name = "Alice"
day = "Monday"
formatted_string = s.format(name, day)
print(formatted_string)

# Using f-strings (Python 3.6+)
formatted_string_f = f"Hello, {name}. Today is {day}."
print(formatted_string_f)


import time;

# Using strftime to format the current time
current_date= time.strftime("%d")
print(f"Today is : {current_date}")
current_month = time.strftime("%B")
print(f"Current month is : {current_month}")  


# number to string conversion
num1 = 123
num2 = 3
print(f"Number as string: {num1 * num2}")


# printing same string 
s = "Hello, World!"
print(f"String: {s}, but if i want to show s as string then i can use {{s}}")