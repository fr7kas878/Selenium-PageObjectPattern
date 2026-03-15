from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "field.email")

class AutenthicationPage(BasePage):

    """
    Authetication Page object
    """
    def enter_create_account_email(self, email):
        """
        enter email for user registration
        :param email:
        :return:
        """



    pass