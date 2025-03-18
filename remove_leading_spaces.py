# Pseudo code:
# 1. Ask for user input
# 2. Remove leading spaces
# 3. Print the cleaned name

def remove_leading_spaces():
    while True:
        name_input = input("Enter your full name: ")
        contains_valid_current_characteracter = False
        
    #Check if input has at least one non-space character
    for current_character in name_input:
            if current_character != ' ':
                has_text = True
                break
            
    if has_text:
        break
    print("Error: Name cannot be only spaces.")