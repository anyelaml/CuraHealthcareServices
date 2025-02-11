from selenium import webdriver
from LocatorsAppointment import FormLocators
from MethodsAppointment import appointmentForm
from LocatorsLogin import LoginPage
from MethodsLogin import LoginPageMethods

class TestAppointmentForm:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        cls.login_page = LoginPageMethods(cls.driver) #importas lading el driver
        cls.appointmentform = appointmentForm(cls.driver)
        cls.selectorsform = FormLocators
        cls.selectors = LoginPage

    def test_login_page(self):
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login()
        assert self.login_page.get_login() == "Facility"

    def test_appointment(self):
        self.appointmentform.complete_form()
        assert self.appointmentform.get_summary() == "Please be informed that your appointment has been booked as following:"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

