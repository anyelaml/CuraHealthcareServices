import time

from LocatorsAppointment import FormLocators
from selenium.webdriver. support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class appointmentForm:
    def __init__(self,driver):
        self.driver = driver
        self.selectors = FormLocators

    def facility_options(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.selectors.facility_options))
        #No se necesita el asterisco porque self.locators.facility  se pasa directamente como un argumento con el presence of element
        self.driver.find_element(*self.selectors.facility_options).click()
        #find_element espera dos argumentos separados:id y el valor pero como argumentos separados en la primera pasa como uno solo.
        #es como si lo desglosaras, porque vienen en paquete.
    def select_facility(self):
        self.driver.find_element(*self.selectors.tokio_health_center).click()

    def select_program(self):
        self.driver.find_element(*self.selectors.medicaid_program).click()

    def visit_date(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.selectors.visit_date))
        self.driver.find_element(*self.selectors.visit_date).click()

    def select_date(self):
        self.driver.find_element(*self.selectors.calendar_date).click()

    def click_book(self):
        self.driver.find_element(*self.selectors.book_button).click()

    def get_summary(self):
        return self.driver.find_element(*self.selectors.summary_text).text


    def complete_form(self):
        self.facility_options()
        self.select_facility()
        self.select_program()
        self.visit_date()
        self.select_date()
        self.click_book()



