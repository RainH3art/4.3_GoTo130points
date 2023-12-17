from .base_page import BasePage
from .locators import PromoPageLocators


class ProductPage(BasePage): 
    
    def remember_book_name(self):
        self.book_name_element = self.browser.find_element(*PromoPageLocators.BOOK_NAME)
        self.book_name =  self.book_name_element.text
        print(self.book_name)

    def remember_book_price(self):
        self.book_price_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE)
        self.book_price =  self.book_price_element.text
        print(self.book_price)
        
    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*PromoPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def fact_book_in_basket_name(self):
        book_in_basket_name_element = self.browser.find_element(*PromoPageLocators.BOOK_IN_BASKET_NAME)
        book_in_basket_name = book_in_basket_name_element.text
        print("Название книги на странице", self.book_name)
        print("Название книги в корзине",book_in_basket_name)
        assert self.book_name in book_in_basket_name, 'Название книги в корзине отличается от добавленной'
        print("Название книги в корзине и название на странице совпадают")
        
    def fact_price_in_basket(self):
        book_price_in_basket_element = self.browser.find_element(*PromoPageLocators.BOOK_PRICE_IN_BASKET)
        book_price_in_basket = book_price_in_basket_element.text
        print("Цена книги", self.book_price)
        print("Сумма в корзине", book_price_in_basket)
        assert self.book_price in book_price_in_basket, 'Цена книги в корзине отличается от указанной при добавлении'
        print("Цена на странице и в корзине совпадает")

        

        

        


        
    
        
    

