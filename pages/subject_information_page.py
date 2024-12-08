from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class SubjectInformationPage(BasePage):
    @property
    def cancel_button(self):
        locator = Locator(by=By.ID, value='tblSubmit_btnTransfer')
        return BaseElement(driver=self.driver, locator=locator)
    
    '''
    Scrapes the data for the subject and returns it as a dictionary.
    '''
    def get_subject_data(self):
        subject_data = {
            'site_number': _safe_get_text(self.driver, By.ID, 'valSiteNum'),
            'subj_id': _safe_get_text(self.driver, By.ID, 'txtScreen'),
            'dob': _safe_get_text(self.driver, By.ID, 'compBirthDate'),
            'sex': _safe_get_text(self.driver, By.ID, 'lstGender', 'Select'),
            'rand_id': _safe_get_text(self.driver, By.ID, 'valRandNum'),
            'prev_treatment': _safe_get_text(self.driver, By.ID, 'lstStrata1'),
            'severity': _safe_get_text(self.driver, By.ID, 'lstStrata2'),
            'cohort': _safe_get_text(self.driver, By.ID, 'lstCohort'),
            'status': _safe_get_text(self.driver, By.ID, 'lstLastActivity'),
            'status_date': _safe_get_text(self.driver, By.ID, 'valActDate'),
            'next_event': _safe_get_text(self.driver, By.ID, 'lstNextActivity')
        }
        return subject_data

'''
Not every patient will have every field present. This function reviews the attempted field and returns the text if the field is present.
'''
def _safe_get_text(driver, by, locator, field_type='Default'):
    try:
        element = BaseElement(driver=driver, locator=Locator(by=by, value=locator))
    except Exception:
        return None

    if field_type == 'Select': # Select/Dropdown fields need to be handled by returned the text that is selected.
        return element.selected_text
    else: # Otherwise, return the text of a default element.
        return element.text