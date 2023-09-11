import unittest
import undetected_chromedriver as uc
import warnings
import urllib3


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = uc.Chrome()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(800, 600)

    def tearDown(self):
        if self.driver is not None:
            print(f'Cleanup Test Environment')
            self.driver.close()
            self.driver.quit()
