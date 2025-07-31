# set is nothing but # unordered collection of unique elements
# set is mutable    

set1 = {1, 2, 3, "raj", 5,True, 3.14}
set2 = {4, 5, 5, 6, 6, 7, 8}


print("Set 1:", set1)
print("Set 2:", set2)

print("Length of Set 1:", len(set1))
print("type",type(set1))

# but 
set3 = {}
print("Type of Set 3:", type(set3))  # This will show it's a dictionary, not a set

# so we should use set() to create an empty set
set3 = set()
print("Type of Set 3 after using set():", type(set3))  # Now it's a set

# loop through a set
for item in set1:
    print(f"item-{item}",item)
