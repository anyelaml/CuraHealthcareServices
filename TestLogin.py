from selenium import webdriver
from LocatorsLanding import LandingPageLocators
from MethodsLanding import LandingPage
from LocatorsLogin import LoginPage
from MethodsLogin import LoginPageMethods

class TestLoginPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        #cls.landing_page = LandingPage(cls.driver)
        cls.login_page = LoginPageMethods(cls.driver)
        #cls.selectors = LandingPageLocators  # aqui guarda los selectores de locators
        # cls es clase.
        cls.selectors_login = LoginPage

    #def test_make_appointment(self):
        #self.landing_page.click_make_an_appointment()
        #assert self.landing_page.get_appointment() == 'Please login to make appointment.'

    def test_login_page(self):
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login()
        assert self.login_page.get_login() == "Facility"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()