# disctionaries methords

# update
d1 = {"name": "raj", "age": 25, "city": "New York"}
d2 = {"age": 30, "country": "USA"}
d1.update(d2)  # Merges d2 into d1, updating existing keys
print("After update:", d1)  


# clear
d1.clear()  # Removes all items from the dictionary
print("After clear:", d1)  # Now d1 is empty    


# copy
d3 = d1.copy()  # Creates a shallow copy of d1
print("Copy of d1:", d3)  # d3 is a copy of d1  

# fromkeys
keys = ["name", "age", "city"]
default_value = "unknown"
d4 = dict.fromkeys(keys, default_value)  # Creates a new dictionary with specified keys and a default value
print("New dictionary from keys:", d4)  # All keys will have the value "unknown"    


# setdefault
d5 = {"name": "raj", "age": 25}
d5.setdefault("city", "New York")  # Sets "city" to "New York" if it doesn't exist
print("After setdefault:", d5)  # If "city" already exists, it won't change its value


# pop
removed_value = d5.pop("age")  # Removes "age" and returns its value
print("Removed age:", removed_value)  # Displays the removed value
print("After pop:", d5)  # Now d5 no longer has the "age" key


# popitem
last_item = d5.popitem()  # Removes and returns the last inserted key-value pair
print("Removed last item:", last_item)  # Displays the removed key-value pair
print("After popitem:", d5)  # Now d5 has one less item


# keys, values, items
print("Keys in d5:", d5.keys())  # Displays all keys in d5
print("Values in d5:", d5.values())  # Displays all values in d5
print("Items in d5:", d5.items())  # Displays all key-value pairs in d5

# get
print("Value for 'name':", d5.get("name"))  # Returns the value for "name"
print("Value for 'country':", d5.get("country", "Not Found"))  # Returns "Not Found" if "country" doesn't exist 


# delete
del d5["name"]  # Deletes the key "name" from d5
print("After delete 'name':", d5)  # Now d5 no longer has the "name" key    


