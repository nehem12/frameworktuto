import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base.drags import Bdrive
from pages.nonstopflight import NonStop
from utilities.flightways import Flight_options

class SearchFlight(Bdrive):
    log = Flight_options.logss()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FROM = "//span[normalize-space()='From']"
    SUGGEST = "//li[@class='react-autosuggest__suggestion']"
    SUGGEST1 = "//li[@class='react-autosuggest__suggestion react-autosuggest__suggestion--first']"
    TO = "//span[normalize-space()='To']"
    DEP = "//span[normalize-space()='Departure']"
    NM = "//span[@aria-label='Next Month']"
    DAT = "//div[@aria-label='Wed Jun 07 2023']//p[contains(text(),'7')]"
    SEA = "//a[normalize-space()='Search']"

    def departcity(self):
        return self.waites(By.XPATH, self.FROM)
    def suggest(self):
        return self.driver.find_elements(By.XPATH, self.SUGGEST)
    def tocity(self):
        return self.waites(By.XPATH, self.TO)
    def suggest1(self):
        return self.driver.find_element(By.XPATH,self.SUGGEST1)
    def ac(self, cli):
        return ActionChains(self.driver).click(cli).perform()
    def depbutton(self):
        return self.waites(By.XPATH, self.DEP)
    def nm(self):
        return self.waites(By.XPATH, self.NM)
    def dat(self):
        return self.waites(By.XPATH, self.DAT)
    def sea(self):
        return self.driver.find_element(By.XPATH, self.SEA)

    def depart(self, dcity):
        flightick = self.departcity()
        self.ac(flightick)
        time.sleep(3)
        fllist = self.suggest()
        for i in fllist:
            if dcity in i.text:
                i.click()
                self.log.info("The depart city is selected")
                break

    def toos(self, tocity):
        flightick = self.tocity()
        self.ac(flightick)
        time.sleep(3)
        fllist2 = self.suggest1()
        fllist3 = self.suggest()
        if tocity in fllist2.text:
          fllist2.click()
          self.log.info("The destination city is selected")
        else:
          for j in fllist3:
            if tocity in j.text:
                j.click()
                self.log.info("The destination city is selected")
                break

        datepick = self.depbutton()
        self.ac(datepick)
        self.log.info("The date section is clicked")
        nemonth = self.nm()
        self.ac(nemonth)
        desdate = self.dat()
        self.ac(desdate)
        self.log.info("The date is selected")
        self.sea().click()

    def sfp(self, dcity, tocity):
        self.depart(dcity)
        self.toos(tocity)
        ns = NonStop(self.driver)
        return ns
