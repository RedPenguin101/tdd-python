# functional_test.py

from selenium import webdriver
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
        self.fail('Finish the test')

        # she is invited to enter a to-do item straight away

        # she types "buy peacock feathers" into a text box

        # when she hits enter the page updates and now the page lists
        # the item in the list

        # there is still a text box, and she enters another item, enters
        # "use peacock feathers to make a fly"

        # the page updates again, it has both items

        # edith doners whether the site will remember her list she sees the site
        # has generated a unique URL for her - there is explanatory text to that
        # effect

        # she visits the url and sees her todo list is still ther

if __name__ == '__main__':
    unittest.main()
