from selenium.webdriver.common.by import By
import pytest
from pages.launchpage import SearchFlight
from utilities.flightways import Flight_options
import unittest
from ddt import ddt,unpack,file_data

@pytest.mark.usefixtures("fisrstone")
@ddt
class Testfly(unittest.TestCase):
    log = Flight_options.logss()
    @pytest.fixture(autouse=True)
    def drives(self):
        self.sf = SearchFlight(self.driver)
        self.ut = Flight_options()

    @file_data("../testdata/testdatayml.yaml")
    @unpack
    def test_c1(self, depcity, descity):
        ns = self.sf.sfp(depcity, descity)
        ns.slelctflight()
        ns.dragss()
        forstop = self.driver.find_elements(By.XPATH, "//p[contains(text(),'Non stop')]")
        self.log.info(len(forstop))
        self.ut.flways(forstop, "Non stop")







