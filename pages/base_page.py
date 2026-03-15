from selenium.webdriver.common.by import By

class BasePage:

#robimy drivera i definicje dla klasy BasePage

    def __init__(self, driver):
        self.driver = driver
        #w momencie  tworzenia definicji verify_page musimy wywoac tu metode
        self._verify_page()

    def _verify_page(self):
        #site autotest
        return
