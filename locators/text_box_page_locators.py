from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.XPATH, "//button[@id='submit']")
    RESULT_SUBMIT = (By.XPATH, "//div[contains(@class, 'border')]")