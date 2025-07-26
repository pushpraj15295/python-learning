# list - nothing but Array

marks = [3,4,6,4,56,0]

val = int(input("check your number is here - "))

if val in marks :
    print("yes matched")
else: print("No match found")



# split [start : end : step]

print(marks[2:5:2])

# generate a list step - init - last 

lists = [i for i in range(10)]
lists1 = [1 for i in range(10)]
lists2 = [i*i for i in range(10)]
lists3 = [i for i in range(10) if(i%2==0)]

print(lists)
print(lists1)
print(lists2)
print(lists3)