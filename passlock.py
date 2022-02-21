import random
import string

import pyperclip

class User:
    """
    create a class that generetes an instance of a user
    """
    user_list = []
    
    
    def __init__(self,username,password):
        """
        a method that defines the properties on the class object 
        """
        
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        test case to check if the user is added to the user list
        '''
        User.user_list.append(self)
    @classmethod   
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)    
class Credentials:
    """
    credential class to help create a new instance of credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user
        
    def __init__(self,account,userName,password):
        """
        test case that check if the credentials are initialized properlyy
        """
        self.account = account
        self.userName = userName
        self.password = password
        
    def save_credentials(self):
        """
        test case to add new credentials 
        """    
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
        
    @classmethod   
    def find_credential(cls,account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
                
    @classmethod
    def if_credential_exist(cls,account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def copy_password(cls,account):
        founded_credentials = Credentials.find_credential(account)
        pyperclip.copy(founded_credentials.password)
    
    # @classmethod
    def generate_password(self):
        """
        generate a random password consisting of numbers,letters and special characters
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(1,9))
