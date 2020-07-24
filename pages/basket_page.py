from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

	#Проверка того, что есть текст о том, что корзина пуста
	def message_basket(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_NONE_BUSKET), \
		"Button is not empty"

	#Проверка того, что в корзине нет товаров 
	def product_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
       "Product in basket, but should not be"
