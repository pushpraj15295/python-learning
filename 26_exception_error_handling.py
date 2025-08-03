# exception error handling is nothing avoiding error while coding 

#  if user enter number then it's fine but wuthout try except if he entered str or boll that time it will throw error

val  = input("please inter number -")

try :
    for i in range(1,5):
        print(i + int(val))
except Exception as err:
# or only except: 
    print("input is invalid" , err) # err will show but aloow to excuter next line
    
except ValueError:
    print("erron in value")
except IndexError:
    print("error in INdex")
    
    
print("your code is fine now")