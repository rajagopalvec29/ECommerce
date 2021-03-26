from utilities.commonfuncs import commonactions

class Loginpage():
    username_id = 'id:=Email'
    password_id = 'id:=Password'
    loginbtn_xpath = 'xpath:=//button[@type = "submit"]'
    logoffbtn_linktext = 'Logout'


    def __init__(self,driver):
        self.driver = driver
        self.commonobj = commonactions(self.driver)

    def setUsername(self,username):
        self.commonobj.clearText(self.username_id)
        self.commonobj.enterText(self.username_id,username)
        # self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setPassword(self,password):
        self.commonobj.clearText(self.password_id)
        self.commonobj.enterText(self.password_id, password)
        # self.driver.find_element_by_id(self.password_id).send_keys(password)

    def Clicklogin(self):
        self.commonobj.uiClick(self.loginbtn_xpath)
        # self.driver.find_element_by_xpath(self.loginbtn_xpath).click()

    def Clicklogoff(self):
        # self.commonobj.uiClick(self.logoffbtn_linktext)
        self.driver.find_element_by_link_text(self.logoffbtn_linktext).click()
