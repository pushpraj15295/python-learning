import time

print(time)

t = time.time()  # Get the current time in seconds since the epoch
print(t)

Ltime = time.localtime()  # Get the current local time
print(Ltime)

t = time.asctime(Ltime)  # Convert local time to a string
print(t)


newTimr = time.strftime("%Y-%m-%d %H:%M:%S")  # Format the time as a string
print(newTimr)