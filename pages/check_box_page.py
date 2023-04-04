from pages.book_page import BasePage
from locators.check_box_page_locators import CheckBoxLocators

class CheckBoxPage(BasePage):
    def check_path(self):
        """Проверка пути"""

        self.element_is_visible(CheckBoxLocators.RCT_OPTION_EXPAND_ALL).click()
        self.element_is_visible(CheckBoxLocators.ANGULAR).click()
        self.element_is_visible(CheckBoxLocators.VEU).click()
        result = self.elements_are_visible(CheckBoxLocators.RESULT)
        result = [i.text for i in result]
        return result