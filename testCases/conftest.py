from selenium import webdriver
import pytest
from utilities.readproperties import ReadConfig
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

baseURL = ReadConfig.GetUrl()
# driver = None

#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail) :
#             file_name = report.nodeid.replace("::", "_")+".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

@pytest.fixture()
def Setup(browser):
    if (browser == 'chrome'):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif (browser == 'firefox'):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif (browser == 'IE'):
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path="E:\chromedriver_new\chromedriver.exe")

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


#
# #scope='session', autouse=True
# @pytest.fixture()
# def Setup():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#
#     driver.maximize_window()
#     driver.get(baseURL)
#     driver.implicitly_wait(5)
#     return driver
