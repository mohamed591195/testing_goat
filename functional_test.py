from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class DjangoInstallation(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # mohamed heard about our todo site
        # he goes to check the home page
        self.browser.get('http://localhost:8000')
        # he found the title of the site says (to-do-list) and in the header
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do list', header_text)

        # he is invited to add a todo item away 
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        #he types 'reading more about TDD in django'
        input_box.send_keys('reading more about TDD in django')
        # when he hits enter the page will update 
        # now the page say you have one item in the list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:reading more about TDD in django' for row in rows),
            'New To-Do item did not appear'
        )
        # there is a still another todo input 
        # he enter applying what i have read
        # he hit enter again and the site update again
        # he wonder if the site will remember him and take the url
        # to reopen it 
        # the site still remebering him
        # finally he is satisfied
        #he quit 
        self.fail('Finish The Test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')