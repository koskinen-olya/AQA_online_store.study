from .pages.product_page import PageObject
from .pages.base_page import BasePage
import pytest

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


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.price_iden()
    product_page.name_iden()
    product_page.correct_message()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.go_to_login_page()