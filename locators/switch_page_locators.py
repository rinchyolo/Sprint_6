from selenium.webdriver.common.by import By


class SwitchPageLocators:
    LOGO_YANDEX = By.XPATH, '//a[contains(@class, "Header_LogoYandex")]/img'  # Логотип "Яндекс" в хедере
    LOGO_SCOOTER = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]/img'  # Логотип "Самокат" в хедере
    DZEN_SEARCH = By.XPATH, '//*[contains(@class, "dzen")]'  # Локатор для дзена

