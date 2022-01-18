import time

import pytest
from selenium.webdriver.common.by import By

from FrameWorkLearn import HomePage, TestData
from FrameWorkLearn.Allgenericmethods import Test_Allgenericmethods
from FrameWorkLearn.FormFields import FormFieldsClass
from FrameWorkLearn.HomePage import HomePageClass
from FrameWorkLearn.TestData import test_TestData
from FrameWorkLearn.productdescriptionclass import ProductDescriptionClass


@pytest.mark.usefixtures("launchbrowser")
class Test_mainclass(Test_Allgenericmethods):
    global ALG
    global Logs
    global PhoneName
    global ProductNameList
    global price
    ALG = Test_Allgenericmethods()
    Logs = ALG.getlogs()

    Logs.info("Browser is launching")
    Logs = ALG.getlogs()
    PhoneName = []
    ProductNameList = []
    price = []



    # def test_URLValue(self):
    #     global InputURL
    #     InputURL = ALG.URLData()
    #     Logs.info(InputURL)


    def test_URLValue(self,test_URLDataUpdated):
        global InputURL
        InputURL = test_URLDataUpdated
        # InputURL = ALG.URLData()
        Logs.info(InputURL)

    def test_setURL(self):
        # Browserdriver.get(InputURL)
        Logs.info("Browser launched successfully")
        self.driver.get(InputURL)



    def test_header(self):

        headervalues = ALG.headerdataset()
        for i in headervalues:
            headerxpath = "//a[contains(text(),'" + i + "')]"
            headerwebelement = self.driver.find_element_by_xpath(headerxpath)

            if headerwebelement.text == i:
                Logs.info(str(headerwebelement.text) + " link exist on home page")
            else:
                Logs.error(str(headerwebelement.text) + " link not exist on home page")


    def test_homepage(self):

        homepage = HomePageClass(self.driver)
        Homepage = homepage.HomePageMethod()

        for i in Homepage:
            Logs.info(str(i.text) + " link exist on side pannel")

    def test_ProductBuy(self):

        productlist = HomePageClass(self.driver)
        ProductList = productlist.productbuy()
        for PhonenameString in ProductList:
            ProductNameList.append(PhonenameString.text)
        j = 0
        for i in ProductList:

            Xpath = "//a[contains(text(),'" + str(ProductNameList[j]) + "')]"
            WEXpath = self.driver.find_element_by_xpath(Xpath)
            ALG.webelementclick(self.driver, WEXpath)
            time.sleep(3)
            productdescname = ProductDescriptionClass(self.driver)
            ProductDescName = productdescname.productdescription()  # to fetch product name

            if ProductDescName.text == ProductNameList[j]:
                Logs.info(str(ProductNameList[j]) + " : Product matches, adding into cart")
                ADDTOCART = productdescname.Addtocartbutton()
                ALG.webelementclick(self.driver, ADDTOCART)
                time.sleep(3)
                Alert = self.driver.switch_to.alert
                Alert.accept()
                Logs.info(str(ProductNameList[j]) + " : Product added into cart")
                LogoImageClick = productdescname.imagelink1()
                ALG.webelementclick(self.driver, LogoImageClick)

            else:
                Logs.error(str(i.text) + ":::::::Product name doesn't match, routing back on home screen")
                LogoImageClick1 = productdescname.imagelink1()
                ALG.webelementclick(self.driver, LogoImageClick1)
                time.sleep(3)
            j = j+1



    def test_cart(self):
        time.sleep(5)
        homepage1 = HomePageClass(self.driver)
        CARTLINK = homepage1.CartLink()
        print(CARTLINK)
        ALG.webelementclick(self.driver, CARTLINK)


    def test_cartpage(self):
        time.sleep(3)
        pricetotal = 0
        for i in ProductNameList:
            j =0
            time.sleep(3)
            ProXpath = "//td[contains(text(),'" + str(i) + "')]"
            ProductWE = self.driver.find_element_by_xpath(ProXpath)
            try:
                if str(i) == str(ProductWE.text):
                    Logs.info(str(i) + ", Product exist on page")
                    homepage2 = HomePageClass(self.driver)
                    PriceXpath = "//tr//td[contains(text(),'"+str(ProductWE.text)+"')]/following-sibling::td"
                    Pricetext = self.driver.find_element_by_xpath(PriceXpath)
                    pricetotal = pricetotal + int(Pricetext.text)


                else:
                    Logs.info("Product not exist")

            except:
                Logs.error("Exception Occoured")

        Logs.info("Total price is : " + str(pricetotal))
        FinalAmount = homepage2.Totalamount()
        if str(pricetotal) == str(FinalAmount.text):
            PlaceOrderButton = self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
            ALG.webelementclick(self.driver, PlaceOrderButton)


    def test_FormVerification(self, Dataset):
        time.sleep(3)
        PurchaseButton = self.driver.find_element_by_xpath("//button[contains(text(),'Purchase')]")
        ALG.webelementclick(self.driver, PurchaseButton)
        time.sleep(1)

        try:

            Alert1 = self.driver.switch_to.alert
            print(Alert1.text)
            Alert1.accept()
            Logs.info("Alert is coming if values not entered")

        except:
            Logs.error("Alert is not coming if value not entered in the field")

        FormFieldsObject = FormFieldsClass(self.driver)
        time.sleep(2)
        FormFieldsObject.FormName().send_keys(Dataset["Name"])
        Logs.info("Name entered successfully")
        FormFieldsObject.FormCountry().send_keys(Dataset["Country"])
        Logs.info("Country entered successfully")
        FormFieldsObject.ForCity().send_keys(Dataset["City"])
        Logs.info("City entered successfully")
        FormFieldsObject.ForCCard().send_keys(Dataset["CreditCardNumber"])
        Logs.info("Credit Card Number entered successfully")
        FormFieldsObject.FormMonth().send_keys(Dataset["Month"])
        Logs.info("Month entered successfully")
        FormFieldsObject.FormYear().send_keys(Dataset["Year"])
        Logs.info("Year entered successfully")
        ALG.webelementclick(self.driver, PurchaseButton)

    def test_Confirmation(self):
        time.sleep(2)
        ConfirmationWindow = FormFieldsClass(self.driver)
        OKBUTTON = ConfirmationWindow.OkButton1()
        ALG.webelementclick(self.driver, OKBUTTON)
        time.sleep(1)
        CurrentURl = self.driver.current_url
        assert CurrentURl == InputURL
        Logs.info("execution over")









