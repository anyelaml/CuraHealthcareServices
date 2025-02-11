from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from LocatorsLogin import LoginPage
from selenium.webdriver.support import expected_conditions as EC
import datalogin

class LoginPageMethods:
    def __init__(self,driver):
        self.driver = driver
        self.locators = LoginPage

    def enter_login(self):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.locators.login_user_name))
        self.driver.find_element(*self.locators.login_user_name).send_keys(datalogin.name)

    def enter_password(self):
        self.driver.find_element(*self.locators.login_password).send_keys(datalogin.password)

    def click_login(self):
        self.driver.find_element(*self.locators.button_login).click()

    def get_login(self):
        return self.driver.find_element(*self.locators.assert_login).text



