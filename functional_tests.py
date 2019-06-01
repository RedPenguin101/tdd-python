# functional_test.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # edith has learned about your new todo app. she goes to the page
        self.browser.get('http://localhost:8000')

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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                'new table row doesnt appear'
                )

        # there is still a text box, and she enters another item, enters
        # "use peacock feathers to make a fly"
        self.fail('finish the test')

        # the page updates again, it has both items

        # edith doners whether the site will remember her list she sees the site
        # has generated a unique URL for her - there is explanatory text to that
        # effect

        # she visits the url and sees her todo list is still ther

if __name__ == '__main__':
    unittest.main()
