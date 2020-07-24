from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    # реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION), "Register form is not presented"
        
    #Регистрация нового пользователя
    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        user_email.send_keys(email)
        user_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        user_password2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_submit.click()

