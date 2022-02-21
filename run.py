#!/usr/bin/env python3.6
from passlock import User,Credentials

def function():    
    print("      _____                           __                             __               ")
    print("   |  _  \                         |  |           __       _____  |  |  __          ")
    print("   | |_)  )  ____   ___   ___      |  |         / __ \    /  ___| |  | /  /         ")
    print("   |  ___/  / _  | / __  / __      |  |        | |  | |  / /      |  |/  /          ")
    print("   |  |    / (_| | \__ \ \__ \     |  |_____   | |__| |  \ \____  |  |\  \          ")
    print("   |__|    \_____|  ___/  ___/     |_______ |   \____/    \_____| |__| \__\         ")  
    print("                                                                                      ")          
function()
 
def create_new_user(username,password):
    '''
    function that creates a user using a password and username
    '''
    new_user = User(username,password) 
    return new_user

def save_user(user):
    '''
    function that saves a new user
    '''
    user.save_user()
def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_user(password,username):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Credentials.verify_user(password,username)
    return checked_user

def create_new_credential(account,userName,password):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    '''
    function that addes a new credential to the credential
    '''
    credentials.save_credentials()
def display_account_details():
    '''
    function that displays user details
    '''
    Credentials.display_credentials()
def delete_credentials(credentials):
    '''
    function that deletes credentials from the credential list
    '''
    credentials.delete_credentials()
def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credentials(account):
    '''
    function that checks if the credentials of the searched name exist and return true or falsd
    '''
    return Credentials.if_credential_exist(account)
def generate_password(self):
    ''' 
    function tht generates password randomely
    '''
    auto_password = Credentials.generate_password(self)
    return auto_password
def copy_password(account):
    '''
    funcion that allows password to be copied and pasted using the pyperclip framework
    '''
    return Credentials.copy_password()


def passlocker():
    print("Hello Welcome to your Accounts Password Locker...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n HA ---  Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == 'ca':
        print("Sign Up")
        print('*' * 50)
        username = input("User_name")
        password = ""
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            pass_choice = input().lower().strip()
            if pass_choice == 'tp':
                print("\n")
                password = input("Enter Password\n")
                break
            elif pass_choice == 'gp':
                password = generate_password(password)
                break
            else:
                print("Invalid password")
        save_user(create_new_user(username,password))
        print("*"*80)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*80) 
    elif short_code == "ha":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username} welcome to password locker manager" )
            print("\n")
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")    
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password(password)
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_details():
                print("Here's your list of acoounts: ")
                
                print('*' * 30)
                print('_'* 30)
                for account in display_account_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password(password)
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passlocker()

