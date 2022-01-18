import inspect
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class AllDataVariable:


    def selectbrowser(self, a):
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument('--start-maximized')
        # ChromeOptions.add_argument('--headless')
        if a == "chrome":
            print(time.localtime())
            print("Chrome is launching....")
            global driver
            driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=ChromeOptions)

        elif a == "firefox":
            print("Firefox browser is not installed")
        else:
            print("IE is not installed")

        return driver

    def URLData (self) :
        File = open('AutomationData')
        Line = File.readline()
        while Line != "":
            if Line.__contains__("url"):
                str1 = Line.split("=")
                print(str1)
                Line = File.readline()

            else:
                print("String not contains #URL hence discontinuing the loop")
                break
        url = str1[1]
        print("url value is: "+url)
        return url

    def writefile(self, b):
        File = open('AutomationOutput')
        content = File.readline()
        while content != "":
            print(content)
            content = File.readline()
            if content =="":
                    with open('AutomationOutput','w') as writer:
                        for i in b:
                            print("Value is:" + b)
                            writer.write(b)
                            File.close()
                            break
            else:
                print("hhh")

    def scriptforgoogleads(self, classname):
        linkclick = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, classname)
            )
        )
        driver.execute_script("arguments[0].click();", linkclick)

    def scriptforgoogleadsLinkText(self, LinkText):
        Xpath = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, LinkText)
            )
        )
        driver.execute_script("arguments[0].click();", Xpath)

    def webelementclick(self,a):
        driver.execute_script('arguments[0].click()',a)

    def alertclick(self,b):
        print(b.text)
        driver.execute_script('arguments[0].click()', b)
        driver.execute_script('')
        b.accept()

    def screenshot(self):
        driver.get_screenshot_as_png()

    def getlogs(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger



