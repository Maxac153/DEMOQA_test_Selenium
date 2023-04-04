from pages.base_page import BasePage
from locators.text_box_page_locators import TextBoxPageLocators

class TextBoxPage(BasePage):
    def filling_fields(self, data):
        """Заполнение формы"""

        self.element_is_visible(TextBoxPageLocators.FULL_NAME).send_keys(data['name'])
        self.element_is_visible(TextBoxPageLocators.EMAIL).send_keys(data['email'])
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS).send_keys(data['current_address'])
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS).send_keys(data['permanent_address'])
        self.element_is_visible(TextBoxPageLocators.SUBMIT).click()

    def submit_form(self, data):
        """Отправка формы"""

        self.filling_fields(data)
        result_submit = self.elements_are_visible(TextBoxPageLocators.RESULT_SUBMIT)
        result_text = [i.text for i in result_submit]
        return result_text

    def check_error_submit(self, data):
        """Проверка на отправку"""

        self.filling_fields(data)
        result_submit = self.element_is_visible(TextBoxPageLocators.EMAIL).get_attribute('class')
        return result_submit
