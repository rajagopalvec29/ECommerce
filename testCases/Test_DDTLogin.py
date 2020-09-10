from pageObjects.LoginPage import Loginpage
from utilities.customLogger import logGen
from utilities import XLUtils
import time
import pytest



class Test_002_DDT_login:
    path = '.\\TestData\\LoginData.xlsx'
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_ddtlogin(self,Setup):
        self.logger.info("***Test_002_DDT_login***")
        self.rownum = XLUtils.getRowCount(self.path, 'Sheet1')
        self.driver = Setup
        loginpage = Loginpage(self.driver)
        loginstatus = []
        a = 1
        for rw in range(2, self.rownum+1):
            username = XLUtils.readData(self.path, 'Sheet1', rw, 1)
            password = XLUtils.readData(self.path, 'Sheet1', rw, 2)
            loginpage.setUsername(username)
            loginpage.setPassword(password)
            loginpage.Clicklogin()
            time.sleep(2)
            logouttext = self.driver.title
            if logouttext == 'Dashboard / nopCommerce administration':
                self.driver.save_screenshot(".\\Screenshots\\" + "loginscreen" + str(a) + ".png")
                loginpage.Clicklogoff()
                self.logger.info("***Login  Success***")
                result = 'Pass'
                loginstatus.append(result)
                XLUtils.writeData(self.path,'Sheet1', rw, 4, result)
                time.sleep(3)
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "loginscreen" + str(a) + ".png")
                self.logger.info("***Login  Failed***")
                result = 'Fail'
                loginstatus.append(result)
                XLUtils.writeData(self.path, 'Sheet1', rw, 4, result)
            a = a + 1

        self.driver.close()
        print(loginstatus)





