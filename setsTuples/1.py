# Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain) and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.

def set_operations_example():
    set_data = {1, 3.14, 'hello', True}
    
    # Demonstrate pop() method
    popped_element = set_data.pop()
    print(f"Popped element: {popped_element}")
    print(f"Updated set after pop(): {set_data}")
    
    # Demonstrate clear() method
    set_data.clear()
    print(f"Set after clear(): {set_data}")
    
    # Re-create the set for demonstration of discard() method
    set_data = {1, 3.14, 'hello', True}
    
    # Demonstrate discard() method
    set_data.discard(3.14)
    print(f"Set after discard(3.14): {set_data}")
    
    # Demonstrate deleting the entire set using 'del'
    del set_data
    # If you try to print(set_data) here, it will raise a NameError since the set no longer exists.


# Calling function
set_operations_example()
