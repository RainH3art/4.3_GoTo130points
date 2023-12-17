from .base_page import BasePage
from .locators import PromoPageLocators


class ProductPage(BasePage): 
    
    def remember_book_name(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_NAME), "Название книги отсутствует"
        self.book_name_element = self.browser.find_element(*PromoPageLocators.BOOK_NAME)
        self.book_name = self.book_name_element.text
        
    def remember_book_price(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_PRICE), "Цена книги отсутствует"
        self.book_price_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE)
        self.book_price =  self.book_price_element.text
        
    def click_on_basket_button(self):
        assert self.is_element_present(*PromoPageLocators.BASKET_BUTTON), "Кнопка добавления в корзину отсутствует"
        basket_button = self.browser.find_element(*PromoPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def fact_book_in_basket_name(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_IN_BASKET_NAME), "Название книги в корзине отсутствует"
        book_in_basket_name_element = self.browser.find_element(*PromoPageLocators.BOOK_IN_BASKET_NAME)
        book_in_basket_name = book_in_basket_name_element.text
        assert self.book_name == book_in_basket_name, f'Название книги в корзине {book_in_basket_name} отличается от добавленной {self.book_name}'
        
    def fact_price_in_basket(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_PRICE_IN_BASKET), "Цена книги в корзине отсутствует"
        book_price_in_basket_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE_IN_BASKET)
        book_price_in_basket = book_price_in_basket_element.text
        assert self.book_price == book_price_in_basket, f'Цена книги в корзине {book_price_in_basket} отличается от указанной при добавлении {self.book_price}'


        

        

        


        
    
        
    

