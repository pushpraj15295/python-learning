age = int(input("please enter your age.."))
name = input("enter your name...")

if(age > 18):
    print("You can drive")
elif(age == 18):
    print("Now you can drive")
else:
    print("Sorry !,You can't drive.")


print("Safe Drive")


# nested if else
if(age == 18) :
    if(len(name)> 5):
        print("Yes")
    else : print("No")