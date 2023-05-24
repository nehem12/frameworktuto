import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.drags import Bdrive
from utilities.flightways import Flight_options

class NonStop(Bdrive):
    log = Flight_options.logss()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    POP = "//button[normalize-space()='OKAY, GOT IT!']"
    FILTER  = "//div[contains(@class,'listingLhs')]//div[1]//div[1]//div[1]//label[1]"

    def pop(self):
        return self.driver.find_element(By.XPATH, self.POP)
    def filter(self):
        return self.waites(By.XPATH, self.FILTER)
    def ac(self, cli):
        return ActionChains(self.driver).click(cli).perform()

    def slelctflight(self):
        self.pop().click()
        self.log.warning("Pop up is closed")
        nonstop = self.filter()
        self.ac(nonstop)
        self.log.warning("Flights are filtered")
        time.sleep(3)
