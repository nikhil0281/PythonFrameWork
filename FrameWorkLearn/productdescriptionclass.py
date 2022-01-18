from selenium.webdriver.common.by import By

class ProductDescriptionClass:

    productname = (By.XPATH, "//h2[@class='name']")
    addcartbutton = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    imagelink = (By.XPATH, "//a[@id='nava']")
    def __init__(self,driver):
        self.driver = driver

    def productdescription(self):
        return self.driver.find_element(*ProductDescriptionClass.productname)

    def Addtocartbutton(self):
        return self.driver.find_element(*ProductDescriptionClass.addcartbutton)

    def imagelink1(self):
        return  self.driver.find_element(*ProductDescriptionClass.imagelink)
