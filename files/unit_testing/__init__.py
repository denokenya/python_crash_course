from distutils.command.build_scripts import first_line_re
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first =input("\nPlease give me a first nme: ")
    if first=='q':
        break
    last = input("Please give me a last name: ")
    if last=='q':
        break
    formatted_name =get_formatted_name(first,last)
    print(f"\tNeatly formatted name:{formatted_name}.")
