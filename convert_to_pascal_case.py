# Pseudo code:
# 1. Get user input
# 2. Convert input to pascal case
# 3. Print the pascal case name

fullname = input("Enter your full name: ")
pascal_case_name = fullname.title().replace(" ", "")
print("Output:", pascal_case_name)