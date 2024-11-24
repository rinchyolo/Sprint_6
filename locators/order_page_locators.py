from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_HEADER = By.XPATH, '//div[contains(@class, "Order_Header")]'  # Хедер для страницы
    BUTTON_COOKIE = By.XPATH, '//button[contains(@class, "App_CookieButton")]'  # Кнопка для принятия куки
    BUTTON_NEXT = By.XPATH, '//button[text()="Далее"]'  # Кнопка "Далее"
    INPUT_NAME = By.XPATH, '//input[contains(@placeholder, "Имя")]'  # Поле для ввода имени
    INPUT_SURNAME = By.XPATH, '//input[contains(@placeholder, "Фамилия")]'  # Поле для ввода фамилии
    INPUT_ADDRESS = By.XPATH, '//input[contains(@placeholder, "Адрес")]'  # Поле для ввода адреса
    INPUT_METRO = By.XPATH, '//input[contains(@placeholder, "метро")]'  # Поле для выбора станции метро
    SELECTOR_METRO = By.XPATH, '//button[contains(@class, "Order_SelectOption")]'  # Селектор для выбора станции метро
    INPUT_PHONE_NUMBER = By.XPATH, '//input[contains(@placeholder, "Телефон")]'  # Поле для ввода номера телефона
    INPUT_COMMENT = By.XPATH, '//input[contains(@placeholder, "Комментарий")]'  # Комментарий для курьера
    BUTTON_ORDER = By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[contains(text(), "Заказать")]'  # Кнопка "Заказать"
    INPUT_RENT = By.XPATH, '//div[@class="Dropdown-placeholder"]'  # Инпут для поля "Срок аренды"
    DROP_DOWN_RENT = By.XPATH, '//div[text()="{}"]'  # Выпадающий список для поля "Срок аренды"
    CHECKBOX_COLOR_GREY = By.ID, 'grey'  # Чекбокс для серого самоката
    INPUT_CALENDAR = By.XPATH, '//input[contains(@placeholder, "привезти")]'  # Инпут для поля "Когда привезти самокат"
    DATE_PICKER_CALENDAR = By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]'  # День в календаре
    BUTTON_MODAL_YES = By.XPATH, '//button[text()="Да"]'  # Кнопка "Да"
    TEXT_MODAL_SUCCESS = By.XPATH, '//*[contains(text(), "Заказ оформлен")]' # Модальное окно успеха
