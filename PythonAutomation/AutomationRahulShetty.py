import time
from logging import exception

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from PythonAutomation.AllDataVariable import AllDataVariable


class ARS(AllDataVariable):

    ALDdriver = AllDataVariable()
    ARSDriver = ALDdriver.selectbrowser("chrome")
    a = ALDdriver.URLData()
    ARSDriver.get(a)
    ARSDriver.maximize_window()
    try:
        ALDdriver.scriptforgoogleads("card-body")
        ALDdriver.scriptforgoogleadsLinkText("//div[@class='header-wrapper']/div[contains(text(),'Forms')]")
        ALDdriver.scriptforgoogleadsLinkText("//span[contains(text(),'Practice Form')]")
        ARSDriver.find_element_by_xpath("//input[@id='firstName']").send_keys("Nikhil")
        ARSDriver.find_element_by_xpath("//input[@id='lastName']").send_keys("Mathur")
        ARSDriver.find_element_by_xpath("//input[@id='userEmail']").send_keys("nikhil@gmail.com")
        time.sleep(2)
        # MaleRadioButton = ARSDriver.find_element_by_xpath("//input[@id='gender-radio-1']")
        # ARSDriver.execute_script('arguments[0].click()',MaleRadioButton)

        Radiobuttons = ARSDriver.find_elements_by_xpath("//div/input[@type='radio']")
        print(len(Radiobuttons))
        # for RadioB in Radiobuttons:
        #     if RadioB.get_attribute("value") == "Female":
        #         RadioB.click
        for i in range(100):
            j=0
            for Radiobutton in Radiobuttons:
                print(Radiobutton)
                ALDdriver.webelementclick(Radiobutton)
                time.sleep(2)

        time.sleep(10)
        ARSDriver.find_element_by_xpath("//input[@placeholder='Mobile Number']").send_keys("9876543210")
        DOB = ARSDriver.find_element_by_xpath("//input[@id='dateOfBirthInput']")
        ALDdriver.webelementclick(DOB)
        ARSDriver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys("23 April 1988")
        ARSDriver.find_element_by_css_selector("input[id='subjectsInput']").send_keys("All")
        checkboxes = ARSDriver.find_elements_by_xpath("//div/input[@type='checkbox']")
        time.sleep(2)
        print(len(checkboxes))
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == 2:
                print("Selecting Reading checkbox....")
                hobbiescheckbox = ARSDriver.find_element_by_xpath("//label[@for='hobbies-checkbox-2']")
                ALDdriver.webelementclick(hobbiescheckbox)

            else:
                print("Selecting sports checkbox....")
                sportscheckbox = ARSDriver.find_element_by_xpath("//label[@for='hobbies-checkbox-1']")
                ALDdriver.webelementclick(sportscheckbox)

        ARSDriver.find_element_by_xpath("//textarea[@class='form-control']").send_keys("Tulip petals, Gurgaon")
       # ARSDriver.find_element_by_xpath("//div[contains(text(),'Select State')]").send_keys("Haryana")
        time.sleep(4)
        Buttontext = ARSDriver.find_element_by_xpath("//button[@id='submit']").text
        print("Button text is : " + Buttontext)

        try:
            ARSDriver.find_element_by_xpath("//button[@id='submit']").click

        finally:
            print("Executing finally block...")
            Submitbutton = ARSDriver.find_element(By.XPATH,"//button[@id='submit']")
            ALDdriver.webelementclick(Submitbutton)

        time.sleep(2)
        closebutton = ARSDriver.find_element_by_id("closeLargeModal")
        ALDdriver.webelementclick(closebutton)




    except exception as e:
        print(e)

