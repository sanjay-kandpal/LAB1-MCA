# Write a python program to display all the datatypes of selected specific elements in the paragraph. (For example:– name - string, reg.no - int, marks - float, etc.)

import re

def identify_data_types_in_paragraph(paragraph):

    # Define regular expression patterns for different data types
    string_pattern = r'([A-Za-z ]+):'
    int_pattern = r'([A-Za-z ]+):\s*(\d+)'
    float_pattern = r'([A-Za-z ]+):\s*(\d+\.\d+)'

    # Find all matches for each data type in the paragraph  
    string_matches = re.findall(string_pattern, paragraph)
    int_matches = re.findall(int_pattern, paragraph)
    float_matches = re.findall(float_pattern, paragraph)

    # Display the results
    print("Data Types:")
    for match in string_matches:
        print(f"{match[0]}: string")

    for match in int_matches:
        print(f"{match[0]}: int")

    for match in float_matches:
        print(f"{match[0]}: float")


# Example paragraph
paragraph = "Name: John Doe, Reg. No: 12345, Marks: 98.5, CGPA: 3.7"

# Call the function to identify data types in the paragraph
identify_data_types_in_paragraph(paragraph)
