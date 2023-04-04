from pages.base_page import BasePage
from locators.frames_page_locators import FramesPageLocators

class FramesPage(BasePage):
    def check_frame(self):
        """Проверка текста"""

        result = self.element_is_visible(FramesPageLocators.HEADING).text
        return result
