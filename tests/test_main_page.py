import allure
import pytest

from data import number_of_questions_and_answers
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize(
        'num, result',
        number_of_questions_and_answers.items()
    )
    @allure.title("Проверка вопроса №{num}")
    def test_check_questions_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.click_on_question(num)
        assert main_page.get_answer_for_question(num) == result
