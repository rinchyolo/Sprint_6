from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTION = By.ID, 'accordion__heading-{}'  # Вопросы в разделе faq
    FAQ_ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'  # Ответы в разделе faq
    FAQ_QUESTION_LAST = By.ID, 'accordion__heading-7'  # Последний вопрос в разделе faq
    BUTTON_HEADER_ORDER = By.XPATH, '//button[text()="Заказать"]'  # Кнопка заказать
    BUTTON_MIDDLE_ORDER = By.XPATH, '//button[contains(@class, "Button_Middle")]'  # Кнопка "Заказать" посередине страницы
    HOME_HEADER = By.XPATH, '//div[contains(@class, "Home_Header")]'  # Блок на главной под хедером