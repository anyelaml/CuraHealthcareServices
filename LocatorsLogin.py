from selenium.webdriver.common.by import By
class LoginPage:
    login_user_name = (By.ID, "txt-username")
    login_password = (By.ID, "txt-password")
    button_login = (By.ID, "btn-login")
    assert_login = (By.CLASS_NAME, "col-sm-offset-3.col-sm-2.control-label")
