import time
from logging import exception

from PythonAutomation.AllDataVariable import AllDataVariable



class demoblaze(AllDataVariable):

    ALDDriver = AllDataVariable()
    DMDriver = ALDDriver.selectbrowser("chrome")
    SiteURL = ALDDriver.URLData()
    PhoneName=[]
    ProductPriceList=[]
    Pricetotal = 0

    # DMDriver.get(SiteURL)
    DMDriver.get(SiteURL)
    DMDriver.maximize_window()
    DMDriver.implicitly_wait(5)

    try:
        print("Logo and header image verification starts....")
        Image = DMDriver.find_element_by_xpath("//a[@id='nava']/img")

        if Image.get_attribute("src") == "https://www.demoblaze.com/bm.png":
            print("Image exists..")
            print(Image.get_attribute("src"))

        else:
            print("Image not exist..")

        Headerlinks = DMDriver.find_elements_by_xpath("//div[@id='navbarExample']//li/a[@class='nav-link']")
        for Headertext in Headerlinks:
            if Headertext.text != "(current)":
                if Headertext.text in "current":
                    HomeHeader = Headertext.text
                    str1= HomeHeader.split(" ")
                    Logs5 = ALDDriver.getlogs()
                    Logs5.info(str1[0] + " link exist")
                    
                elif Headertext.text == "Contact":
                    Logs = ALDDriver.getlogs()
                    Logs.info("Contact Link exist1")
                    #print("Contact link exist")
                elif Headertext.text == "About us":
                    Logs1 = ALDDriver.getlogs()
                    Logs1.info("About us link exist")
                    # print("About us link exist")
                elif Headertext.text == "Cart":
                    Logs2 = ALDDriver.getlogs()
                    Logs2.info("Cart link exist")
                    #print("Cart link exist")
                elif Headertext.text == "Log in":
                    print("Log in link exist")
                elif Headertext.text == "Sign up":
                    print("Sign up link exist")
                else:
                    print(Headertext.text)
            else:
                print("current link exist")

    finally:
        print("Header verification complete")

    try:
        time.sleep(3)
        if DMDriver.find_element_by_xpath("//a[contains(text(),'Phones')]").text == "Phones":
            print("Phone link exist")
            PhonesList = DMDriver.find_elements_by_xpath("//a[@class='hrefch']")

            for PhonenameString in PhonesList:
                print("Phonename is : " + PhonenameString.text)
                PhoneName.append(PhonenameString.text)
            print(PhoneName)

            i = 0
            while i < len(PhonesList):
                PLXpath = "//a[contains(text(),'" + PhoneName[i] + "')]"
                Plname = DMDriver.find_element_by_xpath(PLXpath)
                ALDDriver.webelementclick(Plname)
                Addtocart = DMDriver.find_element_by_xpath("//a[@class='btn btn-success btn-lg']")
                ALDDriver.webelementclick(Addtocart)
                time.sleep(2)
                Alert = DMDriver.switch_to.alert
                Alert.accept()
                time.sleep(2)
                # ProductPrice = DMDriver.find_element_by_class_name("price-container")
                # ProductPriceList.append = ProductPrice
                Homelink = DMDriver.find_element_by_xpath("//a[contains(text(),'Home')]")
                ALDDriver.webelementclick(Homelink)
                # print(ProductPriceList[i])
                i = i+1
                del Plname


        else:
            print("Phones link doesn't exist")
    except:
        print("error:::::::::::")


    try:
        CartLink = DMDriver.find_element_by_xpath("//*[@id='cartur']")
        ALDDriver.webelementclick(CartLink)
        time.sleep(3)
        for ProductsListONCartPage in PhoneName:
            ProductXpath = "//td[contains(text(),'"+ ProductsListONCartPage +"')]"
            PriceXpath = "//tr/td[contains(text(),'" + ProductsListONCartPage + "')]/following-sibling::td"
            ProducrPrice = DMDriver.find_element_by_xpath(PriceXpath)
            ProductsCartList = DMDriver.find_element_by_xpath(ProductXpath)

            assert ProductsCartList.text == ProductsListONCartPage
            print(ProductsListONCartPage + " exist in cart list and price of the product is : " + ProducrPrice.text)
            Pricetotal = Pricetotal + int(ProducrPrice.text)
            print(Pricetotal)
            print("===================================================")

        print("Total price is : " + str(Pricetotal))
        sumtotal = DMDriver.find_element_by_xpath("//h3[@id='totalp']")

        assert sumtotal.text == str(Pricetotal)
        print("Total price matched..")
        PlaceOrderButton = DMDriver.find_element_by_xpath("//button[contains(text(),'Place Order')]")
        ALDDriver.webelementclick(PlaceOrderButton)
        time.sleep(2)
        print(":::::::::::Place Order window verification begins:::::::::::")
        PlaceOrderWindowTitle = DMDriver.find_element_by_xpath("//h5[@id='orderModalLabel']")
        print(PlaceOrderWindowTitle.text)
        assert PlaceOrderWindowTitle.text == "Place order"
        print("Window title matches")
        PurchaseButton = DMDriver.find_element_by_xpath("//button[contains(text(),'Purchase')]")
        ALDDriver.webelementclick(PurchaseButton)
        time.sleep(2)
        Alert = DMDriver.switch_to.alert
        assert Alert.text == "Please fill out Name and Creditcard."
        print("Alert appears for not filling the entries.")
        Alert.accept()

        DMDriver.find_element_by_xpath("//input[@id='name']").send_keys("Nikhil")
        DMDriver.find_element_by_xpath("//input[@id='country']").send_keys("India")
        DMDriver.find_element_by_xpath("//input[@id='city']").send_keys("Delhi")
        DMDriver.find_element_by_xpath("//input[@id='card']").send_keys("000000000")
        DMDriver.find_element_by_xpath("//input[@id='month']").send_keys("April")
        DMDriver.find_element_by_xpath("//input[@id='year']").send_keys("1990")
        ALDDriver.webelementclick(PurchaseButton)

        print(":::::::::: verification of confirmation window begins ::::::::::::")
        time.sleep(2)
        Righticon = DMDriver.find_element_by_xpath("//div[@class='sa-placeholder']")
        Thankyoumessage = DMDriver.find_element_by_xpath("//div[@class='sweet-alert  showSweetAlert visible']/h2")

        if Thankyoumessage.text == "Thank you for your purchasee!!":
            Logs3 = ALDDriver.getlogs()
            Logs3.info("text match")
        else:
            Logs4 = ALDDriver.getlogs()
            Logs4.error("Thank you message text doesn't match")
            Logs4.error(Thankyoumessage)

        print("Thank you for your purchasing with us")
        OkButton = DMDriver.find_element_by_xpath("//button[@class='confirm btn btn-lg btn-primary']")
        ALDDriver.webelementclick(OkButton)
        time.sleep(2)
        Homeurl = DMDriver.current_url
        ALDDriver.screenshot()
        print(Homeurl)

        assert SiteURL == Homeurl
        print("User routes back on home")
        print("User routes back on home2.")
        print(time.localtime())
            # if ProductsCartList.text == ProductsListONCartPage:
            #     print(ProductsListONCartPage + " exist in cart list.....")
            # else:
            #     print(ProductsListONCartPage + " not exist in cart list.....")
            # if ProductsCartList.text == ProductsListONCartPage:
            #     print(ProductsListONCartPage + " exist in cart list.....")

            # ProductsCartList.clear


    finally:
        print("Execution Over")