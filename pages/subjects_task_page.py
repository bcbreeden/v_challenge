from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class SubjectsTaskPage(BasePage):
    @property
    def view_information_link(self):
        locator = Locator(by=By.ID, value='lnkView2')
        return BaseElement(driver=self.driver, locator=locator)