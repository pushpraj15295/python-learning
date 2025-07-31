# mothod for set in python

s1 = {1, 2, 3, "raj", 5, True, 3.14}
s2 = {1,2,2,2,5,4, 5, 6, 7, 8}

print("Set" , s1.union(s2))  # union of two sets
print("Set" , s1.intersection(s2))  # intersection of two sets

print("Set" , s1.difference(s2))  # difference of two sets
print("Set" , s1.symmetric_difference(s2))  # symmetric difference of two sets

# add an item to a set ( one item at a time)
s1.add(10)
print("Set 1 after adding 10:", s1)

# update a set with multiple elements
s1.update(s2)
print("Updated Set 1:", s1)

# remove an item from a set - with Error if not present 
s1.remove(2)  # Raises KeyError if 2 is not found
print("Set 1 after removing 2:", s1)   

# discard an item from a set - without erro if not present
s1.discard(3)  # Does not raise an error if 3 is not found
print("Set 1 after discarding 3:", s1)

# isdistjoin set, issubset and issuperset methods

print("Is Set 1 disjoint with Set 2?", s1.isdisjoint(s2))  # Check if two sets have no elements in common
print("Is Set 1 a subset of Set 2?", s1.issubset(s2))  # Check if all elements of Set 1 are in Set 2
print("Is Set 1 a superset of Set 2?", s1.issuperset(s2))  # Check if Set 1 contains all elements of Set 2


# rendome value pop from a set
popped_item = s1.pop()  # Removes and returns an arbitrary element from the set
print("Popped item from Set 1:", popped_item)
print("Set 1 after popping an item:", s1)

# delete and clear a set
del s1  # Deletes the entire set
# print(s1)  # This will raise a NameError since s1 is deleted  

s1 = {1, 2, 3, "raj", 5, True, 3.14}
s1.clear()  # Clears all elements from the set
print("Set 1 after clearing:", s1)  # Now Set 1 is empty