from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.slider_page_locators import SliderPageLocators

class SliderPage(BasePage):
    def slider_value(self):
        """Значение slider"""

        result_text = self.element_is_visible(SliderPageLocators.SLIDER).get_attribute('value')
        return result_text

    def slider_move(self, move):
        """Перетаскивание slider"""

        slider = self.element_is_visible(SliderPageLocators.SLIDER)
        actions = self.action_chains()
        actions.move_to_element(slider)
        actions.click_and_hold().move_by_offset(move, 0).release().perform()