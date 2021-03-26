import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_login:
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    logger = logGen.loggen()

    def test_homepage(self,Setup):
        self.logger.info("****Test_01_login_test01****")
        self.driver = Setup
        pagetitle = self.driver.title
        if pagetitle == 'Your store. Login':
            allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "homepage.png")
            self.logger.info("****Home page Title verfied****")
            assert True
        else:
            self.logger.error("****Home page Title Not verfied****")
            assert False
        self.driver.close()

    def test_login(self,Setup):
        self.logger.info("****Test_01_login_test02****")
        self.driver = Setup
        self.loginpage = Loginpage(self.driver)
        self.loginpage.setUsername(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.Clicklogin()
        time.sleep(1)
        pagetitle = self.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]")
        if pagetitle.text == 'Dashboards':
            self.logger.info("****Login page Title verfied****")
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Homepage",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\"+"dashboard.png")
            self.logger.error("****Login page Title not verfied****")
            self.driver.close()
            assert False


