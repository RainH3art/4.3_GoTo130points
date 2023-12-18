from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Логин в ссылке отсутствует'
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина отсутствует'
        
    def should_be_register_form(self):
         assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации отсутствует'
         
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_FIELD)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_AGAIN_FIELD)
        pass2_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_MESSAGE), "Сообщение об успешной регистрации отсутствует"