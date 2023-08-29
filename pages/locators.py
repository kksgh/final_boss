from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REG_CHECK_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REG_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration-submit']")
    LOG_EMAIL = (By.CSS_SELECTOR, "[name = 'login-username']")
    LOG_PASSWORD = (By.CSS_SELECTOR, "[name = 'login-password']")
    LOG_SUBMIT = (By.CSS_SELECTOR, "[name = 'login_submit']")
