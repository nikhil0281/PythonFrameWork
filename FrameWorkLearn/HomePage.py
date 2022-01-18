import self
from selenium.webdriver.common.by import By


class HomePageClass:
    sidepanellinks = (By.XPATH, "//a[@id='itemc']")
    productlist = (By.XPATH, "//a[@class='hrefch']")
    cartlink = (By.XPATH, "//a[@id='cartur']")
    PlaceOrderButton = (By.XPATH, "//div/button[@class='btn btn-success']")
    TotalAmount = (By.XPATH, "//h3[@id='totalp']")

    def __init__(self,driver):
        self.driver = driver



    def HomePageMethod(self):
        # print(self.driver.find_element(*HomePageClass.sidepanellinks))
        return self.driver.find_elements(*HomePageClass.sidepanellinks)

    def productbuy(self):
        return  self.driver.find_elements(*HomePageClass.productlist)

    def CartLink(self):
        return self.driver.find_element(*HomePageClass.cartlink)

    def productcompare(self, i):
        ProXpath = "//td[contains(text(),'" + str(i) + "')]"
        return ProXpath

    def productprice(self, productname):
        pricexpath = "//tr//td[contains(text(),'" + productname + " ')]/following-sibling::td[1]"
        return pricexpath

    def placeorder(self):
        return self.driver.find_element(*HomePageClass.PlaceOrderButton)

    def Totalamount(self):
        return self.driver.find_element(*HomePageClass.TotalAmount)


