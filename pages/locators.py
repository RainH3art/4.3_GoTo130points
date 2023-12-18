from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default[href*='basket']")
    
class BasketPageLocators():
    IN_BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    
   