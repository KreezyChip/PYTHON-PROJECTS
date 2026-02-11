import os
os.system("cls")

print("CREATE AN ACCOUNT\n")

''' Loops until user input is valid'''
while True:
    user_name = input("User: ")
    password = input("Password: ")

    ''' Boolean '''
    has_letter = False
    has_number = False
    
    ''' loops and goes through each character in the password variable '''
    for char in password:
            
            ''' checks the character’s Unicode value to see if it’s a letter (a-z or A-Z) or a number (0-9).'''
            if("a" <= char <= "z") or ("A" <= char <= "Z"):
                 has_letter = True
            if "0" <= char <= "9":
                 has_number = True

    '''  If both a letter and a number are found, the password is accepted.  '''
    if has_letter and has_number:
        os.system("cls")
        print("Successfully created an account! Please try to log in\n")
        break
    else:
         os.system("cls")
         print("Password must contain at least one letter and one number! Please Try again!\n")

    

while True:
    
        user = input("Username: ")
        psw = input("Password: ")

        
        if user == user_name and psw == password:
            print("Logged in!")
            break
        else:
            os.system("cls")
            print("Incorrect Username or Password, Please try again!\n")