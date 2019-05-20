from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # mohamed heard about our todo site
        # he goes to check the home page
        self.browser.get(self.live_server_url)
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
        self.check_for_row_in_list_table('1: reading more about TDD in django')
        # there is a still another todo input 
        # he enter applying what i have read
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('applying what i have read')
        # he hit enter again and the site update again
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: reading more about TDD in django')
        self.check_for_row_in_list_table('2: applying what i have read')
        # he wonder if the site will remember him so he took the url
        # to reopen it 
        # the site still remebering him
        # finally he is satisfied
        #he quit 
        self.fail('Finish The Test')

