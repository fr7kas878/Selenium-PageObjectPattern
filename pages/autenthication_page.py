from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "login")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")

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
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)



    def enter_create_account_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.CREATE_ACCOUNT_EMAIL)
        ).send_keys(email)


