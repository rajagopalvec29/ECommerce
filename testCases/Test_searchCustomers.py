import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomer import addCustomers
from pageObjects.SearchCustomers import searchCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import logGen
import time
from pytest_html import extras


class Test_004_searchCustomer:
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    logger = logGen.loggen()
    emailid = 'james_pan@nopCommerce.com'

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_serachbyemail(self,Setup):
        self.driver = Setup
        lp = Loginpage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.Clicklogin()
        addnew = addCustomers(self.driver)
        addnew.Click_customerlink()
        addnew.Click_customersublink()
        search = searchCustomer(self.driver)
        search.serchbyemail(self.emailid)
        search.Clicksearchbtn()
        time.sleep(1)
        search.Getemailtable()

        if self.emailid == search.Getemailtable():
            self.driver.save_screenshot(".\\Screenshots\\searchCustomer.png")
            self.logger.info("*********Search Customer Success")
            assert True
        else:
            assert False
        self.driver.close()




