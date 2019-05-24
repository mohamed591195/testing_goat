from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10
class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_and_wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn( row_text, [row.text for row in rows])
                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # mohamed heard about our todo site
        # he goes to check the home page
        self.browser.get(self.live_server_url)
        # he found the title of the site says (to-do-list) and in the header
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new To-Do list', header_text)

        # he is invited to add a todo item away 
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        #he types 'reading more about TDD in django'
        input_box.send_keys('reading more about TDD in django')
        # when he hits enter the page will update 
        # now the page say you have one item in the list
        input_box.send_keys(Keys.ENTER)
       
        self.check_and_wait_for_row_in_list_table('1: reading more about TDD in django')
        # there is a still another todo input 
        # he enter applying what i have read
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('applying what i have read')
        # he hit enter again and the site update again
        input_box.send_keys(Keys.ENTER)
       
        self.check_and_wait_for_row_in_list_table('1: reading more about TDD in django')
        self.check_and_wait_for_row_in_list_table('2: applying what i have read')
        
        # finally he is satisfied
        #he quit 
        # self.fail('Finish The Test')
        
    def test_multi_users_can_have_unique_lists(self):
        self.browser.get(self.live_server_url)
        input = self.browser.find_element_by_id('id_new_item')
        input.send_keys('reading more about TDD in django')
        input.send_keys(Keys.ENTER)
        self.check_and_wait_for_row_in_list_table('1: reading more about TDD in django')

        # he notices that he has a unique url
        mohamed_list_url = self.browser.current_url
        self.assertRegex(mohamed_list_url, '/lists/.+')
        self.browser.quit()
        # now a new user come to the site called ahmed
        self.browser = webdriver.Firefox()
        
        # now ahmed visit the home page 
        self.browser.get(self.live_server_url)
        # there should be no sign of previous user mohammad
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('reading more about TDD in django', page_text)

        # ahmed start by adding an item to his list
        input = self.browser.find_element_by_id('id_new_item')
        input.send_keys('buying milk')
        input.send_keys(Keys.ENTER)
        self.check_and_wait_for_row_in_list_table('1: buying milk')
        # self.check_and_wait_for_row_in_list_table('reading more about TDD in django')

        # ahmed get his own list url
        ahmed_list_url = self.browser.current_url
        self.assertRegex(ahmed_list_url, '/lists/.+')

        # Again there is no trace of mohammad's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('reading more about TDD in django', page_text)
        self.assertIn('buying milk', page_text)
    
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x'] , 512, delta=10)
        input_box.send_keys('testing')
        input_box.send_keys(Keys.ENTER)
        self.check_and_wait_for_row_in_list_table('1: testing')
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x'], 512, delta=10)
