from pages import base_page
from pages.autenthication_page import AutenthicationPage
from selenium. webdriver.common.by import By




class Locators:
    """
    tu zbieram lokatory do testow
    """
    SIGN_IN_LINK = (By.CLASS_NAME,"login")


class HomePage(base_page.BasePage):
    #dziedziczenie z pliku base_page_klasa Base_page

    """
    Base page object for each page
    """

    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return AutenthicationPage(self.driver)
        #* locatosr to rozpakowanie krotki Locators

