# fanally keyword will always excute in any condition 
# any return or break can't stop finally to excute--


val = int(input("enter num - "))
def fun1():
    try:
        ar = [2,3,5,6,7,9,9,00,2,3,8]
        print(ar[val])
    except:
        return 0
    finally:
        print("Please check with other number")
        
        
ans = fun1()

print(ans)