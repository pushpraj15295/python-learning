# if loop will fully excuted then only else work 
# if loop break in any condition else won't work 

# ex -01
for i in range(6):
    print(i)
 
else:
    print("Loop not break")
    
    
 # ex -02
for i in range(6):
    print(i)
    if(i == 4):break
 
else:
    print("not printed mean loop breaked")   
