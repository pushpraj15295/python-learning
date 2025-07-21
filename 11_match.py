x = int(input("please inter your age - "))


# it swich case but without break.

match x :
    case 10:
        print("your age is less then 18")
    case 18 :
        print("your age is 18")
    case _ if x>18 :
        print("you are mature now")
    case _ :
        print(x)