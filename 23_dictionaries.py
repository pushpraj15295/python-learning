# Dictionaries in python is not a collection of key-value pairs
# Dictionaries are mutable, unordered collections of items
# where each item is stored as a pair of a key and its corresponding value.


dic = {
    "name": "raj",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"]   
}

# Accessing value by key - this will raise KeyError if key not found
print(dic["city"])
# Using get method to access value by key - this will return None if key not found
print(dic.get("name")) 


# get a default value if key not found
print(dic.get("country", "Not Found"))  # Returns "Not Found" if "country" key does not exist

# Adding a new key-value pair
dic["country"] = "USA"
print("After adding country:", dic)
# Updating an existing key-value pair
dic["age"] = 31 
print("After updating age:", dic)


# other dictionary methods
dic.pop("is_student")  # Removes the key "is_student" and returns its value
print("After popping is_student:", dic)
dic.popitem()  # Removes and returns the last inserted key-value pair
print("After popping last item:", dic)

# Looping through dictionary ----------------------------------------------------------------loop in dictionary
for key, value in dic.items():
    print(f"Key: {key}, Value: {value}")
    
# Creating an empty dictionary
empty_dic = {}
print("Empty Dictionary:", empty_dic)   

    
    
print("Dictionary:", dic)
print("Type of Dictionary:", type(dic))
print("Length of Dictionary:", len(dic))
print("Keys in Dictionary:", dic.keys())
print("Values in Dictionary:", dic.values())
print("Items in Dictionary:", dic.items())


# loop in only keys ---------------------------------------------------------------------loop in keys
for key in dic:
    print(f"Key: {key}, Value: {dic[key]}")  # Accessing value using key    
    
    
# or you can use the keys() method
for key in dic.keys():
    print(f"Key: {key}, Value: {dic[key]}")  # Accessing value using key

# loop in only values ---------------------------------------------------------------------loop in values
for value in dic.values():
    print(f"Value: {value}")  # Directly accessing value
    
# or you can use the values() method
for value in dic.values():
    print(f"Value: {value}")  # Directly accessing value
    
    