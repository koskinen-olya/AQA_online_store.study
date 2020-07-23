from .locators import ProductPageLocators
from .base_page import BasePage

class PageObject(BasePage):
	#Проверяем существование кнопки, нажимаем на неё
	def add_product(self):
		assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button is not presented"
		button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
		button.click()
	#Цена на сайте и в корзине одинаковая?
	def price_iden(self):
		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
		book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
		assert book_price == book_price_in_basket, 'No ident price'
	#Имя товара на сайте и в корзине одинаковое?
	def name_iden(self):
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
		book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
		assert book_name == book_name_in_basket, 'No ident name'
	#
	def correct_message(self):
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
		message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
		assert book_name in message, 'Dont correct message'




