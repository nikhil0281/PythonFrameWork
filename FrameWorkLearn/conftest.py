import time

import pytest



# class dataset():
from selenium import webdriver

from FrameWorkLearn.TestData import test_TestData


@pytest.fixture()
def headerdataset(self):
    headertext = ["Contact","About us","Cart","Log in","Sign up"]
    return  headertext


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--url_value", action="store", default="dv")



@pytest.fixture(scope="class")
def launchbrowser(request):
    # a = "chrome1"
    global driver
    browser_name = request.config.getoption("browser_name")
    ChromeOptions = webdriver.ChromeOptions()
    ChromeOptions.add_argument('--start-maximized')
    FireFoxOptions = webdriver.FirefoxOptions()
    FireFoxOptions.add_argument('--start-maximized')
    # ChromeOptions.add_argument('--headless')
    if browser_name == "chrome":
        (time.localtime())
        print("Chrome is launching....")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=ChromeOptions)

    elif browser_name == "firefox":
        print("firefox is launching....")
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=FireFoxOptions)
    else:
        print("IE is not installed")
    driver.implicitly_wait(5)


    request.cls.driver = driver

@pytest.fixture()
def test_URLDataUpdated(request):
    LifeCycle = request.config.getoption("url_value")
    if LifeCycle == "dv":
            url = "https://www.demoblaze.com/index.html"
    elif LifeCycle == "qa":
            url = "https://www.google.com"
    else:
            url = "https://yahoo.com"
    return url

@pytest.fixture(params=test_TestData.test_testdata)
def Dataset(request):
    return request.param