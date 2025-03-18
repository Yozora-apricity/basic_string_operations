# Pseudo code:
# 1. Get a number from the user
# 2. Validate the range
# 3. Format and print the number

def format_six_digits():
    while True:
        try:
            user_number_input = input("Enter a number (0-1000): ")
            converted_integer_number = int(user_number_input)
            
            if 0 <= converted_integer_number <= 1000:
                break
            print("Error: Number out of range. Try again.")
        except ValueError:
            print("Error: Invalid input. Enter a valid number.")