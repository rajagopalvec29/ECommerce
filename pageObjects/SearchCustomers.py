from utilities.commonfuncs import commonactions



class searchCustomer:
    txtSearchemail_id = 'id:=SearchEmail'
    tableGrid_xpath  = '//table[@id="customers-grid"]'
    tablerow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tablecolumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    btnsearch_id = 'id:=search-customers'



    def __init__(self,driver):
        self.driver = driver
        self.commonobj = commonactions(self.driver)

    def serchbyemail(self,email):
        self.commonobj.enterText(self.txtSearchemail_id,email)
        # self.driver.find_element_by_id(self.txtSearchemail_id).send_keys(email)

    def Clicksearchbtn(self):
        self.commonobj.uiClick(self.btnsearch_id)
        # self.driver.find_element_by_id(self.btnsearch_id).click()

    def Getemailtable(self):
        self.rows = len(self.driver.find_elements_by_xpath(self.tablerow_xpath))
        for rw in range(1,self.rows+1):
            table = self.driver.find_element_by_xpath(self.tableGrid_xpath)
            res_email = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(rw)+"]/td[2]").text
            return res_email



