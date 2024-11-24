import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Создание заказа')
    def fill_form_to_order_scooter(self, name, surname, address, metro, phone, rental_period, comment):
        self.allow_cookie()
        self.set_first_name(name)
        self.set_second_name(surname)
        self.set_address(address)
        self.set_metro_station(metro)
        self.set_phone_number(phone)
        self.click_button_next()
        self.set_date()
        self.set_rental_period(rental_period)
        self.set_color()
        self.set_comment_for_courier(comment)
        self.click_button_order()

    @allure.step('Заполнение поля "Имя"')
    def set_first_name(self, name):
        self.enter_text(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_second_name(self, surname):
        self.enter_text(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.enter_text(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Заполнение поля "Номер телефона"')
    def set_phone_number(self, phone):
        self.enter_text(OrderPageLocators.INPUT_PHONE_NUMBER, phone)

    @allure.step('Выбор станции метро')
    def set_metro_station(self, metro):
        self.enter_text(OrderPageLocators.INPUT_METRO, metro)
        self.click_on_element(OrderPageLocators.SELECTOR_METRO)

    @allure.step('Тап на кнопку "Далее"')
    def click_button_next(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Выбор даты для привоза самоката')
    def set_date(self):
        self.click_on_element(OrderPageLocators.INPUT_CALENDAR)
        self.click_on_element(OrderPageLocators.DATE_PICKER_CALENDAR)

    @allure.step('Выбор срока аренды')
    def set_rental_period(self, rental_period):
        self.click_on_element(OrderPageLocators.INPUT_RENT)
        element = self.format_locators(OrderPageLocators.DROP_DOWN_RENT, rental_period)
        self.click_on_element(element)

    @allure.step('Выбор цвета самоката')
    def set_color(self):
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_GREY)

    @allure.step('Ввод комментария для курьера')
    def set_comment_for_courier(self, comment):
        self.enter_text(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Заказ самоката')
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_MODAL_YES)

    @allure.step('Получение результата заказа самоката')
    def get_result_for_order(self):
        return self.wait_element_and_check_displayed(OrderPageLocators.TEXT_MODAL_SUCCESS)

    @allure.step('Принятие кук')
    def allow_cookie(self):
        self.wait_for_element(OrderPageLocators.ORDER_HEADER)
        self.click_on_element(OrderPageLocators.BUTTON_COOKIE)
