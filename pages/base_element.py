from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BaseElement(object):
    '''
    The Base Element object holds shared functions and properties that is shared across the various elements.

    args:
        Driver: WebDriver
        Locator: The locator used to return the element.
        Index: If there is a list of elements returned, this argument will specifiy which to return. Default: 0
    '''
    def __init__(self, driver, locator, index=0):
        self.driver = driver
        self.locator = locator
        self.index = index

        self.web_element = None
        self.find()

    def find(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator=self.locator)
        )
        self.web_element = elements[self.index]
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        text = self.web_element.text
        return text
    
    @property
    # Selected text from a dropdown.
    def selected_text(self):
        element = Select(self.web_element)
        selected_option = element.first_selected_option.text
        return selected_option