from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.remember_book_name()
    page.remember_book_price()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    page.fact_book_in_basket_name()
    page.fact_price_in_basket()
    
    # pytest -v -s .\test_product_page.py

