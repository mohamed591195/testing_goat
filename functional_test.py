from unittest import TestCase
import unittest
from selenium import webdriver

class DjangoInstallation(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # mohamed heard about our todo site
        # he goes to check the home page
        self.browser.get('http://localhost:8000')
        # he found the title of the site says (to-do-list)
        self.assertIn('To-Do lists', self.browser.title)
        self.fail('Finish The Test')
        # he is invited to add a todo item away 
        #he types reading more about TDD in django 
        # when he hits enter the page will update 
        # now the page say you have one item in the list
        # there is a still another todo input 
        # he enter applying what i have read
        # he hit enter again and the site update again
        # he wonder if the site will remember him and take the url
        # to reopen it 
        # the site still remebering him
        # finally he is satisfied
        #he quit 
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')