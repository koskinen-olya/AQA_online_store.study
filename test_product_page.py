from .pages.product_page import PageObject
from .pages.base_page import BasePage
import pytest

@pytest.mark.xfail
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
