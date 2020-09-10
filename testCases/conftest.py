from selenium import webdriver
import pytest
from utilities.readproperties import ReadConfig

baseURL = ReadConfig.GetUrl()

@pytest.fixture()
def Setup(browser):
    if (browser == 'chrome'):
        driver = webdriver.Chrome(executable_path="E:\\chromedriver_win32\\chromedriver.exe")
    elif(browser == 'IE'):
        driver = webdriver.Edge(executable_path="C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="E:\\chromedriver_win32\\chromedriver.exe")

    driver.maximize_window()
    driver.get(baseURL)
    driver.implicitly_wait(5)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



####### pytest HTML REPORT ######
#it is hook for adding env variable in html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E Commerce'
    config._metadata['Module Name']  = 'Customer'
    config._metadata['Tester Name'] = 'Raja'

#it is hook to update or modify the env variable in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)
    metadata.pop('Plugins', None)
    metadata.pop('Python', None)

