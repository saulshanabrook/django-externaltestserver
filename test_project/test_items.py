import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from externaltestserver import ExternalLiveServerTestCase

from items.models import Item


class IntegrationTest(ExternalLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor=os.environ['SELENIUM_HOST'],
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_item_count(self):
        Item.objects.create()
        self.browser.get(self.live_server_url)
        self.assertIn("1", self.browser.page_source)

    def test_item_count_2(self):
        Item.objects.create()
        Item.objects.create()
        self.browser.get(self.live_server_url)
        self.assertIn("2", self.browser.page_source)

    def test_static_file(self):
        self.browser.get(self.live_server_url + 'static/items/test.txt')
        self.assertIn("test", self.browser.page_source)
