import allure

from pages.base_page import BasePage


class SwitchPage(BasePage):
    @allure.step('Клик на картинку в хедере')
    def click_image_on_header(self, locator):
        self.click_on_element(locator)

    @allure.step('Проверка открытия необходимой страницы')
    def check_element(self, locator):
        self.switch_to_window()
        return self.wait_element_and_check_displayed(locator)
