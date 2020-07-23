from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
	BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
	BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
	BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
	BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")