from .base_page import BasePage
from .locators import PromoPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.on_page_book_name()
        self.on_page_book_price()
        self.click_on_basket_button()
        self.solve_quiz_and_get_code()
        self.fact_book_in_basket_name()
        self.fact_price_in_basket()
        self.should_be_name_the_same()
        self.should_be_price_the_same()
    
    def on_page_book_name(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_NAME), "Элемент название книги отсутствует"
        self.book_name_element = self.browser.find_element(*PromoPageLocators.BOOK_NAME)
        self.book_name = self.book_name_element.text
        
    def on_page_book_price(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_PRICE), "Элемент цена книги отсутствует"
        self.book_price_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE)
        self.book_price =  self.book_price_element.text
        
    def click_on_basket_button(self):
        assert self.is_element_present(*PromoPageLocators.BASKET_BUTTON), "Кнопка добавления в корзину отсутствует"
        basket_button = self.browser.find_element(*PromoPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def fact_book_in_basket_name(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_IN_BASKET_NAME), "Название книги в корзине отсутствует"
        self.book_in_basket_name_element = self.browser.find_element(*PromoPageLocators.BOOK_IN_BASKET_NAME)
        self.book_in_basket_name = self.book_in_basket_name_element.text
        
    def fact_price_in_basket(self):
        assert self.is_element_present(*PromoPageLocators.BOOK_PRICE_IN_BASKET), "Цена книги в корзине отсутствует"
        self.book_price_in_basket_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE_IN_BASKET)
        self.book_price_in_basket = self.book_price_in_basket_element.text

    def should_be_name_the_same(self):   
        assert self.book_name == self.book_in_basket_name, f'Название книги в корзине {self.book_in_basket_name} отличается от добавленной {self.book_name}'     
    
    def should_be_price_the_same(self):
        assert self.book_price == self.book_price_in_basket, f'Цена книги в корзине {self.book_price_in_basket} отличается от указанной при добавлении со страницы {self.book_price}'
    


        

        

        


        
    
        
    

