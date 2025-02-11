from selenium.webdriver.common.by import By

class FormLocators:
    facility_options = (By.CSS_SELECTOR, "#combo_facility.form-control")
    tokio_health_center = (By.XPATH, "//option[@value='Tokyo CURA Healthcare Center']")
    medicaid_program = (By.CSS_SELECTOR, "#radio_program_medicaid")
    visit_date = (By.ID, "txt_visit_date")
    calendar_date = (By.XPATH, "/html/body/div/div[1]/table/tbody/tr[4]/td[3]")
    book_button = (By.ID, "btn-book-appointment")
    summary_text = (By.CLASS_NAME, "lead")

