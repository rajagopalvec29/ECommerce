from selenium import webdriver
import pytest
import time
from utilities.commonfuncs import commonactions



class CustomerRole:
    linkCustrole = "//span[text()='Customer roles']"
    custtablexpath = '(//table)[2]'
    chooseproductxpath = "//button[contains( text(),'Choose product')]"
    taxcheckid = 'TaxExempt'
    freeshippingid = 'FreeShipping'
    savebtn = 'save'


    def __init__(self,driver):
        self.driver = driver
        self.commonobj = commonactions(self.driver)

    def ClickCustRole(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.linkCustrole).click()
        self.commonobj.take_screenshots('CustRole')

    def ClickEdit(self,role):
        time.sleep(2)
        editlink = self.driver.find_element_by_xpath("(//table)[2]//tr//td[text() = '{}']//following::td[5]".format(role))
        editlink.click()
        self.commonobj.take_screenshots('EditRole')

    def ClickProduct(self,product):
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.chooseproductxpath).click()
        winhands = self.driver.window_handles
        self.driver.switch_to.window(winhands[1])
        self.driver.find_element_by_id('SearchProductName').send_keys('PC')
        self.driver.find_element_by_id('search-products').click()
        time.sleep(1)
        self.commonobj.take_screenshots('SearchProductRole')
        prosel = self.driver.find_element_by_xpath("//td[contains(text(),'{}')]//preceding::td[1]".format(product))
        prosel.click()
        self.driver.switch_to.window(winhands[0])
        self.driver.find_element_by_id(self.taxcheckid).click()
        self.driver.find_element_by_id(self.freeshippingid).click()
        self.driver.find_element_by_name(self.savebtn).click()
        self.commonobj.take_screenshots('ProductRole')
        self.driver.close()

