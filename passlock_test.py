import unittest
from passlock import User,Credentials

class TestClass(unittest.TestCase):
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User("","qwertykey")
        
    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,'Daniel Muthama')
        self.assertEqual(self.new_user.password,'qwertykey')
        
    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has neen created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.new_credentials = Credentials('Gmail','Daniel Muthama','qwertykey')
        
    def test_ini_(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        
        self.assertEqual(self.new_credentials.account,'Gmail')
        self.assertEqual(self.new_credentials.userName,'Daniel Muthama')
        self.assertEqual(self.new_credentials.password,'qwertykey') 
        
    def test_save_credentials(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
        
    def test_save_many_account(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","muthama","Mfh45hfk")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
        
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_credentials()
        test_credential =  Credentials("Twitter","muthama","Mfh45hfk")
        test_credential.save_credentials()
        
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","muthama","Mfh45hfk")
        test_credential.save_credentials()
        
        the_credential = Credentials.find_credential("Twitter")
        self.assertEqual(the_credential.account,test_credential.account)
        
    
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","muthama","Mfh45hfk")
        test_credential.save_credentials()
        
        found_credential = Credentials.if_credential_exist("Twitter")
        self.assertTrue(found_credential)
        
    def test_display_all_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''
        
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
if __name__ == '__main__':
        unittest.main()
        