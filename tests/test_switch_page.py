import allure
import pytest

from locators.main_page_locators import MainPageLocators
from locators.switch_page_locators import SwitchPageLocators
from pages.main_page import MainPage
from pages.switch_page import SwitchPage


@allure.title("Проверка клика по логотипам")
class TestSwitchPage:
    @pytest.mark.parametrize(
        'locator_image, locator_page',
        [[SwitchPageLocators.LOGO_YANDEX, SwitchPageLocators.DZEN_SEARCH],
         [SwitchPageLocators.LOGO_SCOOTER, MainPageLocators.HOME_HEADER]]
    )
    def test_check_click_on_image(self, driver, locator_image, locator_page):
        main_page = MainPage(driver)
        switch_page = SwitchPage(driver)
        main_page.click_order_button()
        switch_page.click_image_on_header(locator_image)
        assert switch_page.check_element(locator_page)
