import allure
import pytest

from data import user_data_1, user_data_2
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title("Тесты на проверку заказа")
class TestOrderPage:

    @pytest.mark.parametrize(
        'user_data, locator',
        [[user_data_1, MainPageLocators.BUTTON_HEADER_ORDER],
         [user_data_2, MainPageLocators.BUTTON_MIDDLE_ORDER]]
    )
    def test_check_order_with_different_data(self, driver, user_data, locator):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_order_button(locator)
        order_page.fill_form_to_order_scooter(**user_data)
        assert order_page.get_result_for_order()
