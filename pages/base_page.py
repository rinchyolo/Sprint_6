from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_and_check_displayed(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).is_displayed()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def switch_to_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
