l = [1,3,4,5,3,6,7,4,2,4,3]

# list methods
print(l)
print(len(l))  # length of the list
print(l[2])  # access element at index 2
print(l[-1])  # access last element
print(l[2:5])  # slice from index 2 to 4
print(l[2:5:2])  # slice with step of 2
l.append(10)  # push
print("append",l)
l.insert(2, 100)  # push to any index
print("insert" ,l)
l.extend([11, 12, 13])  # push multi items
print("extend",l)
l.remove(100)  # remove first occurrence of 100
print(l)
l.pop()  # remove last element
print(l)
l.pop(2)  # remove element at index 2
print("remove on index",l)
l.clear()  # clear the list
print(l)


# Reinitialize the list to demonstrate further methods
l = [1, 3, 4, 5, 3, 6, 7, 4, 2, 4, 3]  # reinitialize the list
print("index of 7 is -", l.index(7))  # find index of first occurrence of 7
print(l.count(3))  # count occurrences of 3
print("count of 3 - ", l.count(3))
l.sort()  # sort the list
print("sort", l)
l.reverse()  # reverse the list
print("reverse", l)
l2 = l.copy()  # copy the list
print("copy", l2)


# add to list 
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # concatenate lists
print("add to list", c)