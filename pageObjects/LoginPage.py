

class Loginpage():
    username_id = 'Email'
    password_id = 'Password'
    loginbtn_xpath = '//input[@type = "submit"]'
    logoffbtn_linktext = 'Logout'


    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def Clicklogin(self):
        self.driver.find_element_by_xpath(self.loginbtn_xpath).click()

    def Clicklogoff(self):
        self.driver.find_element_by_link_text(self.logoffbtn_linktext).click()
