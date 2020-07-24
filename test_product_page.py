from .pages.product_page import PageObject
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

#Данный класс регистрирует новых пользователей и проверяет 2 тест-кейса: отстутсвие сообщения о добавлении товара в корзину, и корректное добавление товара в корзину
@pytest.mark.user_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        email = str(time.time()) + "@fakemail.org"
        password = 'koskinenolya'
        product_page = PageObject(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        product_page2 = LoginPage(browser, browser.current_url)
        product_page2.register_new_user(email,password)
        product_page2.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        product_page = PageObject(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        product_page = PageObject(browser, link)
        product_page.open()
        product_page.add_product()
        product_page.price_iden()
        product_page.name_iden()
        product_page.correct_message()

#Данный тест кейс проверяет отсутсвие сообщения о добавлении в корзину 
def test_guest_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

#Данный тест кейс проверяет корректное добавление в корзину
def test_guest_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.price_iden()
    product_page.name_iden()
    product_page.correct_message()

#Данный тест кейс проверяет корректное добавление в корзину промо товара 
@pytest.mark.skip
def test_on_promo(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.price_iden()
    product_page.name_iden()
    product_page.correct_message()

#Данный тест кейс проверяет что сообщение о добавлении товара в корзину НЕ появилось после добавления в корзину (т.е. заранее провален)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_not_be_success_message()

#Данный тест кейс проверяет что сообщение о добавлении товара в корзину исчезнет после добавления в корзину (т.е. заранее провален)
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_dissapear_of_success_message()

#Проверяет наличие формы входа со страницы продукта
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_be_login_link()

#Переходит на форму входа со страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.go_to_login_page()
#Проверяет, что со страницы товара можно перейти в корзину и она будет пуста
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.go_to_basket()
    product_page2 = BasketPage(browser, browser.current_url)
    product_page2.product_basket()
    product_page2.message_basket()