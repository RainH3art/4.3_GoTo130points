from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.IN_BASKET_ITEM), "Element in Items found, but should be not"
        
    def should_be_text_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text of empty basket presented"