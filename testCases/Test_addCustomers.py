import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomer import addCustomers
from utilities.readproperties import ReadConfig
from utilities.customLogger import logGen



class Test_003_Add_customers:
    username = ReadConfig.GetUsername()
    password = ReadConfig.GetPassword()
    email_id = addCustomers.random_generator() + "@gmail.com"
    password_id = "raja123"
    firstname_id = "Raja"
    lastname_id = "devi"
    dob_id = '9/9/1990'
    companyname = 'Verizon'
    vendor = 'Vendor 1'
    comments = 'This is first time'
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,Setup):
        self.driver = Setup
        lp = Loginpage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.Clicklogin()
        addnew = addCustomers(self.driver)
        addnew.Click_customerlink()
        addnew.Click_customersublink()
        addnew.Click_addcustomer()
        addnew.set_emailid(self.email_id)
        addnew.set_password(self.password_id)
        addnew.set_firstname(self.firstname_id)
        addnew.set_lastname(self.lastname_id)
        addnew.set_gender()
        addnew.set_dob(self.dob_id)
        addnew.set_companyname(self.companyname)
        addnew.set_taxempt()
        addnew.add_letterlist()
        addnew.add_rolelist()
        addnew.dd_vender(self.vendor)
        addnew.set_comments(self.comments)
        addnew.Click_savebtn()
        time.sleep(1)
        self.msg = self.driver.find_element_by_tag_name("body").text
        if 'The new customer has been added successfully.' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "Addcustomerscreen.png")
            self.logger.info("*****The new customer has been added successfully")
            assert True
        else:
            self.logger.info("*****Cutomers are not added")

        self.driver.close()