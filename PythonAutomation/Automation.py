from logging import exception

from selenium import webdriver

# File = open('AutomationData')
# Line = File.readline()
# str1=""
#
# while Line != "":
#     print(Line)
#     str1 = Line.split("=")
#     Line = File.readline()
#     print(str1[1])
#
# url= str1[1]
# print(url)
from self import self

from PythonAutomation.AllDataVariable import AllDataVariable


class Automation(AllDataVariable):

    DataClassObject = AllDataVariable()  # DataClassObject is a object or instance of AlldataVariable class
    Driverfocus = DataClassObject.selectbrowser("chrome") # Driverfocus is a variable which contains driver value from AllDataVariable class
    a = DataClassObject.URLData()
    Driverfocus.get(a)
    PageTitle = Driverfocus.title
    WebPageTitle = "Page title is : " + PageTitle + "\n"
    DataClassObject.writefile("ABCCCC")




    # try:
    #     Driverfocus.find_element_by_id("user-name").send_keys("standard_user")
    #     Driverfocus.find_element_by_name("password").send_keys("secret_sauce")
    #     Driverfocus.find_element_by_name("login-button").click()
    #     PageTitle = Driverfocus.find_element_by_class_name("title").text
    #     print(PageTitle)
    # except exception as e:
    #     print(e)
    #     print("============================================================================")

    try:
        Driverfocus.implicitly_wait(10000)
        Username = Driverfocus.find_element_by_xpath("//form[@name='login']/div[1]/label").text
        Usernametext = Username + " text exist on login window11\n"
        DataClassObject.writefile(Usernametext)
        Driverfocus.find_element_by_link_text("Forgot Your Password?").click()
        print("Login Page title")
    except exception as e:
        print(e)
        print("=============================================================================")







