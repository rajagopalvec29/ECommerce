import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.readproperties import ReadConfig
from pageObjects.LoginPage import Loginpage
from pageObjects.RoleCustomers import CustomerRole
from pageObjects.AddCustomer import addCustomers
import allure

class Test_005_Custoles:
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    role = 'Guests'
    product = 'Lenovo'

    def test_customersRoles(self,Setup):
        self.driver = Setup
        lp = Loginpage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.Clicklogin()
        sc = addCustomers(self.driver)
        sc.Click_customerlink()
        cr = CustomerRole(self.driver)
        cr.ClickCustRole()
        cr.ClickEdit(self.role)
        cr.ClickProduct(self.product)












