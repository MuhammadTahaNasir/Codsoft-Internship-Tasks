import random
import string


# Function to generate a random password
def generate_password(length):

    # Define a set of characters consisting of letters and digits
    characters = string.ascii_letters + string.digits

    # Generate a password without a special character first
    password = ''.join(random.choice(characters) for _ in range(length - 1))

    # Add one special character at the end of the password
    password += random.choice(string.punctuation)

    # Randomly shuffle the characters in the password to enhance security
    return ''.join(random.sample(password, len(password)))


# Function to generate and display a password
def generate_and_display_password():
    print("")
    print("   ***************************************************")
    print("            WELCOME TO THE PASSWORD GENERATOR         ")
    print("   ***************************************************")

    print(''' 
       Instructions:
    - Define the desired password length.
    - Include uppercase letters, digits, and special characters in the password.
    - Customize the password complexity to suit your needs.

           *** We are set to generate a password to bolster your security! ***\n''')

    # Ask the user to choose the complexity of the password
    while True:
        complexity = input("Select password complexity (weak, moderate, or strong): ").lower()

        if complexity == 'strong':
            while True:
                password_length = int(input("Enter the length of the password (greater than 8): "))
                if password_length <= 8:
                    print("Invalid input: Password length for strong complexity must be greater than 8.")
                else:
                    break
            break
        elif complexity == 'moderate':
            while True:
                password_length = int(input("Enter the length of the password (6-8): "))
                if not (6 <= password_length <= 8):
                    print("Invalid input: Password length for moderate complexity must be between 6 and 8.")
                else:
                    break
            break
        elif complexity == 'weak':
            while True:
                password_length = int(input("Enter the length of the password (less than 6): "))
                if password_length >= 6:
                    print("Invalid input: Password length for weak complexity must be less than 6.")
                else:
                    # Provide a warning about the security risks of weak passwords
                    print("Warning: Weak passwords can be easy to hack.")
                    response = input("Do you still want to generate a weak password? (yes/no): ").lower()
                    if response != 'yes':
                        break
                    else:
                        break
            break
        else:
            print("Invalid complexity. Please choose 'weak', 'moderate', or 'strong'.")

    # Generate the password based on user's complexity and length choice
    generated_password = generate_password(password_length)
    print("Generated Password: ", generated_password)

    print('Congratulations! Your password has been created.')
    print("Thanks for using! Have a good day")


# Execute the password generation and display
generate_and_display_password()
