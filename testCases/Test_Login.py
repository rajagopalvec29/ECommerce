import time
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_login:
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_homepage(self,Setup):
        self.logger.info("****Test_01_login_test01****")
        self.driver = Setup
        pagetitle = self.driver.title
        if pagetitle == 'Your store. Login':
            self.driver.save_screenshot(".\\Screenshots\\" + "homepage.png")
            self.driver.close()
            self.logger.info("****Home page Title verfied****")
            assert True
        else:
            self.driver.close()
            self.logger.error("****Home page Title Not verfied****")
            assert False

    @pytest.mark.sanity
    def test_login(self,Setup):
        self.logger.info("****Test_01_login_test02****")
        self.driver = Setup
        self.loginpage = Loginpage(self.driver)
        self.loginpage.setUsername(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.Clicklogin()
        time.sleep(1)
        pagetitle = self.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]")
        if pagetitle.text == 'Dashboard':
            self.logger.info("****Login page Title verfied****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"dashboard.png")
            self.logger.error("****Login page Title not verfied****")
            self.driver.close()
            assert False

