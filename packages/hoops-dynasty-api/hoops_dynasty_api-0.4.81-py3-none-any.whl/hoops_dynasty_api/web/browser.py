from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class WebBrowser():

    def __init__(self):
        #print('creating uc browser')
        self.chrome_driver_version = '125.0.6422.141'
        self.browser = self.build_web_browser()
        self.wis_url = 'https://www.whatifsports.com/locker/'
        self.login_url = 'https://idsrv.fanball.com/login'
        #self.wis_login_button_class = 'Link__ButtonLink-fXkPwX'

        #self.login_to_wis()


    def build_web_browser(self): # -> webdriver:
        """ builds a webbrowser

        :return: a selenium webbrowser object
        """
        # chrome_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'utils/chromedriver89'))
        # chrome_path = '/usr/local/bin/chromedriver'
        #print('setting up options')
        options = uc.ChromeOptions()
        #options.add_argument('start-maximized')
        #options.add_argument('--user-data-dir=/Users/zach/Library/Application Support/Google/Chrome/Default')
        #options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        #options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--headless')
        browser = self._build_browser(options)
        #print('browser completed')
        return browser


    def open_url(self, url: str):
        if self.browser:
            self.browser.get(url)
        else:
            # todo custom error here
            print("there is no browser")

    def open_and_soup(self, url: str):
        if self.browser:
            self.browser.get(url)
            soup = BeautifulSoup(self.browser.page_source, 'html.parser')  # Parse the page source
            return soup
        else:
            # todo custom error here
            print("there is no browser")

        return False


    def _build_browser(self, options: uc.ChromeOptions, retry_count: int = 0) -> webdriver:
        #try:
        browser = uc.Chrome(options=options, use_subprocess=False)
        #except SessionNotCreatedException:
        #    raise WebBrowserCreationError()
        
        return browser
    
    def page_source(self):
        return self.browser.page_source

    def get_user_credentials(self):
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        return username, password

    def login_to_wis(self):
        print('logging into wis')
        self.browser.get(self.login_url)
        try:
            self.browser.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()
        except NoSuchElementException:
            pass
        self.browser.find_element(By.LINK_TEXT, 'Login').click()
        #self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/label/input').click()

        username_input = self.browser.find_element(By.ID, 'username')
        
        password_input = self.browser.find_element(By.ID, 'password')
        username, password = self.get_user_credentials()
        username_input.send_keys(username)
        password_input.send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, 'g-recaptcha.button--primary')
        # todo add exception handling here for if login fails
        self.open_url(self.wis_url)
        self.browser.find_element_by(By.LINK_TEXT, 'VMI').click()
