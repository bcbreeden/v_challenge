from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class MenuNavigationPage(BasePage):
    @property
    def admin_link(self):
        locator = Locator(by=By.LINK_TEXT, value='Admin')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def admin_inventory_link(self):
        locator = Locator(by=By.LINK_TEXT, value='Inventory')
        return BaseElement(driver=self.driver, locator=locator)