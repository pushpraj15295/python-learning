tap = (1,211,3,4,5,6,7,8,9,10)  # tuple - immutable list
print(tap)
print(len(tap))  # length of the tuple
print(tap[2])  # access element at index 2
print(tap[-1])  # access last element
print(tap[2:5])  # slice from index 2 to 4
print(tap[2:5:2])  # slice with step of 2   

if 3 in tap:  # check if 3 is in the tuple
    print("yes matched")
else:
    print("No match found")



# we cannot modify tuples as they are immutable
# Uncommenting the following lines will raise errors

# tap.append(10)  # tuples do not support append
# print("append", tap)  # this will raise an error  
# tap.insert(2, 100)  # tuples do not support insert
# print("insert", tap)  # this will raise an error
# tap.extend([11, 12, 13])  # tuples do not support extend
# print("extend", tap)  # this will raise an error

# but we can convert a tuple to a list, modify it, and then convert it back to a tuple
tap_list = list(tap)  # convert tuple to list
tap_list.append(10)  # now we can append
print("append to list converted from tuple", tap_list)
tap_list.insert(2, 100)  # insert into the list
print("insert to list converted from tuple", tap_list)
tap_list.extend([11, 12, 13])  # extend the list
print("extend to list converted from tuple", tap_list)  
# convert back to tuple
tap = tuple(tap_list)  # convert list back to tuple
print("converted back to tuple", tap)

tap.index(7, 0, len(tap))  # find index of first occurrence of 7
print("index of 7 is -", tap.index(7))  # find index of first occurrence of 7
print(tap.count(3))  # count occurrences of 3
print("count of 3 - ", tap.count(3))  # count occurrences of


