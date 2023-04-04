from pages.base_page import BasePage
from locators.droppable_page_locators import DroppablePageLocators

class DroppablePabe(BasePage):
    def check_draganddrop(self):
        """Проверка перемещения элемента"""

        drop = self.element_is_visible(DroppablePageLocators.DROPPABLE)
        drog = self.element_is_visible(DroppablePageLocators.DROGGABLE)
        self.drag_and_drop(drog, drop)
        return drop.text