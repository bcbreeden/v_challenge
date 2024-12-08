from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class LoginPage(BasePage):
    @property
    def login_field(self):
        locator = Locator(by=By.ID, value='txtLogin')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def password_field(self):
        locator = Locator(by=By.ID, value='txtPassword')
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def login_button(self):
        locator = Locator(by=By.ID, value='btnLogin')
        return BaseElement(driver=self.driver, locator=locator)