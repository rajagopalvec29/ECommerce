from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

class addCustomers:
    customer_link = "(//li/a/p[contains(text(),'Customers')])[1]"
    cus_sublink = "(//li/a/p[contains(text(),'Customers')])[2]"
    addnew_customer = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    email_id = "Email"
    password_id = "Password"
    firstname_id = "FirstName"
    lastname_id = "LastName"
    radio_male = "Gender_Male"
    dob_id = "DateOfBirth"
    companyname_id = "Company"
    taxexempt_id = "IsTaxExempt"
    newsletter_xpath = "(//input[@role='listbox'])[1]"
    teststore_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[2]'
    roles_xpath = "(//input[@role='listbox'])[2]"
    guest_xpath = '//li[text()="Guests"]'
    DD_vender_id = 'VendorId'
    comment_id = "AdminComment"
    save_btn = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def Click_customerlink(self):
        self.driver.find_element_by_xpath(self.customer_link).click()

    def Click_customersublink(self):
        self.driver.find_element_by_xpath(self.cus_sublink).click()

    def Click_addcustomer(self):
        self.driver.find_element_by_xpath(self.addnew_customer).click()

    def set_emailid(self,email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def set_password(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def set_firstname(self,firstname):
        self.driver.find_element_by_id(self.firstname_id).send_keys(firstname)

    def set_lastname(self,lastname):
        self.driver.find_element_by_id(self.lastname_id).send_keys(lastname)

    def set_gender(self):
        self.driver.find_element_by_id(self.radio_male).click()

    def set_dob(self,dob):
        self.driver.find_element_by_id(self.dob_id).send_keys(dob)

    def set_companyname(self, companyname):
        self.driver.find_element_by_id(self.companyname_id).send_keys(companyname)

    def set_taxempt(self):
        self.driver.find_element_by_id(self.taxexempt_id).click()

    def add_letterlist(self):
        self.driver.find_element_by_xpath(self.newsletter_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.teststore_xpath).click()

    def add_rolelist(self):
        self.driver.find_element_by_xpath('//*[@id="SelectedCustomerRoleIds_taglist"]/li[1]/span[2]').click()
        self.driver.find_element_by_xpath(self.roles_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.guest_xpath).click()

    def dd_vender(self,vendor):
        self.vendorlist = self.driver.find_element_by_id(self.DD_vender_id)
        self.selectvendor = Select(self.vendorlist)
        self.selectvendor.select_by_visible_text(vendor)

    def set_comments(self,comments):
        self.driver.find_element_by_id(self.comment_id).send_keys(comments)

    def Click_savebtn(self):
        self.driver.find_element_by_xpath(self.save_btn).click()

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))