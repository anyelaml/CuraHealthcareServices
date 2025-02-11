from selenium import webdriver
from LocatorsLanding import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage:
    def __init__(self,driver):
        #inicializador, va siempre primero para que pueda funcionar el driver y dar click
        self.driver = driver
        self.selectors = LandingPageLocators #aqui se guardan todos los selectores en una variable para solo llamarlo despues

    def click_make_an_appointment(self):
    #si importo la clase, saco todos los localizadores, pero puedo llamar solo a uno de los localizadores si quiero
    #si me interesan todas las clases de un archivo llamo a todas las  clase pero si solo me interesa uno llamo directo
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.selectors.button_make_appointment))
        self.driver.find_element(*self.selectors.button_make_appointment).click()

    def get_appointment(self):
        #con esto estoy regresando o pidiendo que me den el texto del localizador de hacer una reserva. que es please....
        return self.driver.find_element(*self.selectors.get_apppointment).text




