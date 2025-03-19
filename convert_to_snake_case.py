# Pseudo code:
# 1. Get user input
# 2. Convert input to snakecase
# 3. Print the snakecase name

fullname = input("Enter your full name: ")
snake_case_name = fullname.lower().replace(" ", "")
print("Output:", snake_case_name)