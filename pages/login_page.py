from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        # реализуйте проверку на корректный url адрес
        CURRENT_URL = self.browser.current_url
        assert "login" in CURRENT_URL, "It is a login page"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOG_EMAIL), "Loginform is present"
        assert self.is_element_present(*LoginPageLocators.LOG_PASSWORD), "Login password is present"
        assert self.is_element_present(*LoginPageLocators.LOG_SUBMIT), "Login submit button is present"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Register email form is present"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Register password form is present"
        assert self.is_element_present(*LoginPageLocators.REG_CHECK_PASSWORD), "Register check password form is present"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT), "Register submit button is present"
        assert True