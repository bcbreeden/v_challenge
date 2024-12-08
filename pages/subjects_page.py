from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class SubjectsPage(BasePage):
    '''
    Attempts to select a subject from the table based on an index (starting at 0 for the first subject listed, etc)
    '''
    def select_subject_by_index(self, subject_index):
        try:
            locator = Locator(by=By.CSS_SELECTOR, value='.fa-gen.menu')
            element = BaseElement(driver=self.driver, locator=locator, index=subject_index)
            element.click()
        except Exception as e:
            print('Subject not found, verify the correct index is provided and that the table has data.')
            print('Index provided:', subject_index)
            print('Exception:', e)