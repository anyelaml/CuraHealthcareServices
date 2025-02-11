from selenium import webdriver
from LocatorsLanding import LandingPageLocators
from MethodsLanding import LandingPage
from LocatorsLogin import LoginPage
from MethodsLogin import LoginPageMethods


class TestLandingPage:
    driver = None
    #Inicia desde cero

    # decorador, lo que abre y cierra la pagina, todo lo que esta dentro lo hace si o si
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome() #esto es para que pueda abrir y hacer acciones en chrome
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/")
        #aqui estoy jalando el driver de aqui no el de la carpeta de methods
        cls.landing_page = LandingPage(cls.driver)
        cls.login_page = LoginPageMethods(cls.driver) #inicializador de login
        # la clase LandingPage toma el controlador del navegador en su
        # constructor (__init__) para poder interactuar con la página de aterrizaje de la aplicación.
        #esta jalando el construit init de methods para que pueda interactuar
        cls.selectors = LandingPageLocators #aqui guarda los selectores de locators
        #cls es clase.
        cls.selectors_login = LoginPage
    def test_make_appointment(self):
        self.landing_page.click_make_an_appointment()
        assert self.landing_page.get_appointment() == 'Please login to make appointment.'
        #con el assert estoy llamando a la funcion de get de la clase landing para que verifique el texto


    def test_login_page(self):
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
