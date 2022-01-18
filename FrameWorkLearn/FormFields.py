from selenium.webdriver.common.by import By


class FormFieldsClass():
    Name = (By.XPATH, "//input[@id='name']")
    Country = (By.XPATH, "//input[@id='country']")
    City = (By.XPATH, "//input[@id='city']")
    CCard = (By.XPATH, "//input[@id='card']")
    Month = (By.XPATH, "//input[@id='month']")
    Year = (By.XPATH, "//input[@id='year']")
    OkButton = (By.XPATH, "//button[@class='confirm btn btn-lg btn-primary']")

    def __init__(self,driver):
        self.driver = driver

    def FormName(self):
        return self.driver.find_element(*FormFieldsClass.Name)

    def FormCountry(self):
        return self.driver.find_element(*FormFieldsClass.Country)

    def ForCity(self):
        return self.driver.find_element(*FormFieldsClass.City)

    def ForCCard(self):
        return self.driver.find_element(*FormFieldsClass.CCard)

    def FormMonth(self):
        return self.driver.find_element(*FormFieldsClass.Month)

    def FormYear(self):
        return self.driver.find_element(*FormFieldsClass.Year)

    def FormPurchaseButton(self):
        return self.driver

    def OkButton1(self):
        return self.driver.find_element(*FormFieldsClass.OkButton)
