# Code complied by S Fanner - 881039191 on 29/05/23
# The code below is a simple Log in Program for Gelos

# -------->Messages dictionary<----------------
message_dict = {
    "new_user_message": """  
_____________________________
Incorrect details
Please register as a new user
    """,
    "loggedin_message": """
_______________________________
You have successfully logged in
    """,
    "error_pwd_message": """
______________________
Incorrect password
    """,
    "loggedout_message": """
    _____________________________
    Goodbye

    You are now logged out!
    _____________________________
                """,
    "invalid_message": """
Invalid option
Please try again

            """,
    "pwd_parameter_message": """
    Passwords must :
    -be a min of 8 characters
     """,
    "summary_message": """
_____________________________
Summary of user account details
_____________________________
        """
}


# -------->Login menu function<----------------
def login_menu():
    """This is a directory of different menu options"""
    print("""
LOG IN MENU
_______________________________
    """)
    menu = ['A. Log in existing user', 'B. Register a new user',
            'C. View summary of all user details', 'D. Exit']
    print(*menu, sep="\n")


# --------> User journey starts here with log in menu <----------------
login_menu()
user_choice = input("Choose your option:")

# --------> Option A - option for logging in existing user<----------------
if user_choice.upper() == "A":
    username = input("What is your username: ")
    # opening accounts file and reading line by line
    for line in open("accounts.txt", "r").readlines():
        split_item = line.split()    # splitting username and password by whitespace
        if username == split_item[0]:
            user_pwd = input("What is your password: ")
            if user_pwd == split_item[1]:   # right username & right password
                print(message_dict["loggedin_message"])
            else:   # right username & wrong password
                print(message_dict["error_pwd_message"])
                user_pwd = input("Try again : ")  # need to work out how to loop back to log in or retry
            break
        print(message_dict["new_user_message"])

        login_menu()
        break

# --------> Option B - option for registering new user<----------------
elif user_choice.upper() == "B":
    username = input("Please enter a username: ")
    user_pwd_choice = input("""
Select an option for your password
(U) User generated or (R) Randomly generated
""")
    if user_pwd_choice.upper() == "U":  # option for creating your own password
        user_pwd = input("Please enter your own password - min 8 characters: ")
        pwd_length = len(user_pwd)

        while pwd_length < 8:  # Password conditions - min 8 characters
            user_pwd = input("Invalid, try again : ")

            if len(user_pwd) >= 8:  # bigger than 8
                print(message_dict["loggedin_message"])
            break
    else:  # option for generated password
        import secrets
        import string  # Need to import to use string operations

        # Define character types
        def generate_pwd(pwd_length, l, n, s):
            characters = ''
            if l:
                characters += string.ascii_letters
            if n:
                characters += string.digits
            if s:
                characters += string.punctuation

            if not characters:
                print("Error: At least one character must be selected. ")
                return None

            user_pwd = ''.join(secrets.choice(characters) for _ in range(pwd_length))
            return user_pwd

        # Users to choose password length & character types
        PWD_LENGTH = int(input("How many characters would you like - choose between 8 to 14?"))

        L = input("Include letters (y/n): ").lower() == 'y'
        N = input("Include numbers (y/n): ").lower() == 'y'
        S = input("Include symbols (y/n): ").lower() == 'y'

        # Generate password
        user_pwd = generate_pwd(PWD_LENGTH, L, N, S)
        if user_pwd:
            print("Generated Password:", user_pwd)
            print(message_dict["loggedin_message"])

    # write username and password to accounts.txt file
    with open("accounts.txt", "a") as file:
        file.write("\n" + username + " " + user_pwd)

# --------> Option C - option for a summary of accounts file<----------------
elif user_choice.upper() == "C":
    with open("accounts.txt", "r") as file:
        print(message_dict["summary_message"])
        print(file.read())

# --------> Option D - option for exit<----------------
elif user_choice.upper() == "D":
    import time
    time.sleep(2)
    print(message_dict["loggedout_message"])

# --------> options for anything else<----------------
else:
    print(message_dict["invalid_message"])
    login_menu()
