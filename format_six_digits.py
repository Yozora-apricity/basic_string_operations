# Pseudo code:
# 1. Get a number from the user
# 2. Validate the range
# 3. Format and print the number

def format_six_digits():
    while True:
        try:
            user_number_input = int(input("Enter a number (0-1000): "))
            
            if 0 <= user_number_input <= 1000:
                break
            print("Error: Number out of range. Try again.")
        except ValueError:
            print("Error: Invalid input. Enter a valid number.")