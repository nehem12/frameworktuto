import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Bdrive():
    def __init__(self, driver):
        self.driver = driver
    DRAGS = "window.scrollTo(0,document.body.scrollHeight)"

    def drags(self):
        return self.driver.execute_script(self.DRAGS)

    def dragss(self):
        self.drags()
        self.drags()
        self.drags()
        time.sleep(3)
    def waites(self, locator, element):
        self.wait = WebDriverWait(self.driver, 20)
        waitscheck = self.wait.until(EC.element_to_be_clickable(self.driver.find_element(locator,element)))
        return waitscheck


