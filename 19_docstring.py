# docsting is nothing but a string that is used to document a function, class, or module.
# It is a way to provide information about what the function or class does, its parameters,
# return values, and any other relevant details. Docstrings are typically written in a specific format
# and can be accessed using the `__doc__` attribute of the function or class.
# just after the function or class definition, enclosed in triple quotes (""" or '''). then only it will be considered as docstring.

def example_function(param1, param2):   
    """
    This is an example function that demonstrates how to use docstrings.

    Parameters:
    param1 (int): The first parameter.
    param2 (int): The second parameter.

    Returns:
    int: The sum of param1 and param2.
    
    Example:
    5
    """ 
    return param1 + param2   

# Accessing the docstring of the function
print(example_function.__doc__)
print("Example function output:", example_function(2, 3))

