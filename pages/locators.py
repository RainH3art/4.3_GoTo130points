from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    
class PromoPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    BOOK_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    BOOK_IN_BASKET_NAME = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(., 'has been added to your basket')]//strong")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']//*[contains(text(), 'Your basket total is now')]//strong")

    
   