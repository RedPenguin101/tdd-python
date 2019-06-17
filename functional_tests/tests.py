# functional_test.py

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
import unittest

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # edith has learned about your new todo app. she goes to the page
        self.browser.get(self.live_server_url)

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        # she types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter the page updates and now the page lists
        # the item in the list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # there is still a text box, and she enters another item, enters
        # "use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        # she types "use peacock feathers to make a fly" into a text box
        inputbox.send_keys('Use peacock feathers to make a fly')

        # when she hits enter the page updates and now the page lists
        # both items one after the other
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table(
                '2: Use peacock feathers to make a fly'
                )

        # edith wonders whether the site will remember her list she sees the
        # site has generated a unique URL for her - there is explanatory
        # text to that effect
        self.fail('finish the test')

        # she visits the url and sees her todo list is still ther
