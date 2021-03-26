import allure
from allure_commons.types import AttachmentType
import os
import datetime

class commonactions:

    def __init__(self,driver):
        self.driver = driver

    def uiClick(self,element):
        values = element.split(':=')
        webobject = values[1]

        if values[0] == 'xpath':
            self.driver.find_element_by_xpath(webobject).click()
        elif values[0] == 'id':
            self.driver.find_element_by_id(webobject).click()

    def enterText(self,element,strdesc):
        values = element.split(':=')
        webobject = values[1]

        if values[0] == 'xpath':
            self.driver.find_element_by_xpath(webobject).send_keys(strdesc)
        elif values[0] == 'id':
            self.driver.find_element_by_id(webobject).send_keys(strdesc)

    def clearText(self,element):
        values = element.split(':=')
        webobject = values[1]

        if values[0] == 'xpath':
            self.driver.find_element_by_xpath(webobject).clear()
        elif values[0] == 'id':
            self.driver.find_element_by_id(webobject).clear()

    def take_screenshots(self,filename):
        allure.attach(self.driver.get_screenshot_as_png(), name=filename, attachment_type=AttachmentType.PNG)

    def make_logfolder(self):
        x = datetime.datetime.now()
        a = x.strftime('%d%m%y')
        b = x.strftime('%H%M%S')
        if os.path.exists('C:\\Users\\Admin\\PycharmProjects\\ECommerce\\Screenshots\\' + str(a)) == True:
            os.makedirs("C:\\Users\\Admin\\PycharmProjects\\ECommerce\\Screenshots\\" + str(a) + "\\" + str(b))
        else:
            os.makedirs("C:\\Users\\Admin\\PycharmProjects\\ECommerce\\Screenshots\\" + str(a))
            os.chdir("C:\\Users\\Admin\\PycharmProjects\\ECommerce\\Screenshots\\" + str(a))
            os.makedirs(str(b))




