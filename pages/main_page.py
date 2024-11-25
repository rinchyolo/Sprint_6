import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на вопрос')
    def click_on_question(self, num):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTION_LAST)
        question = self.format_locators(MainPageLocators.FAQ_QUESTION, num)
        self.click_on_element(question)

    @allure.step('Получение ответа на вопрос')
    def get_answer_for_question(self, num):
        answer = self.format_locators(MainPageLocators.FAQ_ANSWER, num)
        return self.get_text(answer)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_order_button(self, locator=MainPageLocators.BUTTON_HEADER_ORDER):
        self.scroll_to_element(locator)
        self.click_on_element(locator)
