# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"

# Step 2: Function that uses the custom exception
def apply_for_job(age):
    if age < 18 or age > 60:
        raise InvalidAgeError(age)
    else:
        print("Application submitted successfully!")

# Step 3: Handling the exception
try:
    user_age = int(input("Enter your age: "))
    apply_for_job(user_age)
except InvalidAgeError as e:
    print(f"Custom Error Caught: {e}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("Thank you for applying.")
