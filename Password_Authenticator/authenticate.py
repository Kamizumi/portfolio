class Password:
    def validate(self, password):
        #initializes count variable so that we can only go up to 3 tries
        count = 0
        while count < 3:
            #checks to see if the input is between 5 and 8 characters and if its first character is capitalized
            if 5 <= len(password) <= 8 and password[0].isupper():
                #checks to see if there is at least one digit in the given password
                hasDigit = any(char.isdigit() for char in password)
                #checks to see if there is at least one symbol in the given password
                hasSymbol =  any(not char.isalnum() for char in password)
                #if hasDigit and hasSymbol are true, then accept password
                if hasDigit and hasSymbol:
                    print("Password is valid. \n")
                    return True
                #if only hasDigit is true, we are missing a symbol, 
                elif hasDigit:
                    print("Missing symbol in password. \n")
                    
                #if only hasSymbol is true, we are missing a digit, 
                elif hasSymbol:
                    print("Missing digit in password. \n")
                    
                #if we are missing both
                else:
                    print("Missing digit and symbol. \n")
            #exits the if loop if password is not between 5 and 8 characters and first letter isn't capitalized        
            else:
                print("Password length is not between 5 and 8 characters and first letter must be capitalized \n")
            #increases count to exit loop
            count += 1
            #checks to see if count is less than or equal to three and asks user to reinput their password
            if count < 3:
                password = input("Please provide a valid passcode: \n")
        #exits while loop as all attempts have been used to validate the password
        print("All attempts have been used\n")
        return False
    
    def create_account(self, username, password):
        #checks to see if the username has already been created
        if username in self.account:
            print("Username already exists\n")
        #if the username doesn't exist, it checks to see if the password they gave is valid
        else:
            validty = self.validate(password)
            #if valid, create the account and put it into the dictionary
            if validty:
                print("Account created.\n")
                self.account[username] = password
            
    
    def login(self, username):
        #checks if username is in the dictionary so that we can check to see if passwords match
        if username in self.account:
            #takes in the password
            password = input("Please input your password: \n")
            #if the password matches the key, then the login is successful
            if self.account[username] == password:
                print("Login successful\n")
            #the password didn't match the key, so the login is unsucessful
            else:
                print("Login was unsuccessful; Password is incorrect.\n")
        #if the username isn't found in the dictionary, print username not found
        else:
            print("Username not found. \n")
            
    def __init__(self):
        #initializes a new dictionary each time it runs
        self.account = {}
    

    def main(self):
        #the while statement allows it to loop until user types in E to exit
        while True:
            #takes in the input of the user
            response = input("Hello user, would you like to login or create a new account (L for login and C for new account | E for exit): \n")
            #exits if input is e
            if response[0].lower() == 'e':
                break
            #prompts login if input is l
            elif response[0].lower() == 'l':
                self.login(input("Please provide a valid username: \n"))
            #prompts creation of new account if input is c
            elif response[0].lower() == 'c':
                #takes in a new username
                username = input("Please create an appropriate username: \n")
                #takes in a new password
                password = input("Please create a valid password (5-8 characters, capitalized first letter, has at least one digit and one symbol)\n")
                #passes username and password into the function of create_account
                self.create_account(username,password)
            #user didn't type one of the letters to prompt a response
            else:
                print("Please choose of one the letters. \n")
            



#initialize the class
pm = Password()
#runs main
pm.main()
