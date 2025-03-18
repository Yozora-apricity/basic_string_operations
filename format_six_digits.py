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
    
    #Manually adding leading zeros in front     
    number_as_string = str(user_number_input)
    while len(number_as_string) < 6:
        number_as_string = "0" + number_as_string
        
    print("Output:", number_as_string)

format_six_digits()