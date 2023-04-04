from selenium.webdriver.common.by import By

class CheckBoxLocators:
    RCT_OPTION_EXPAND_ALL = (By.XPATH, "//button[contains(@class, 'rct-option-expand-all')]")
    ANGULAR = (By.XPATH, "//span[contains(text(), 'Angular')]")
    VEU = (By.XPATH, "//span[contains(text(), 'Veu')]")
    RESULT = (By.XPATH, "//div[@id='result']")