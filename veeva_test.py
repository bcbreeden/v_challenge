from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.login_page import LoginPage
from pages.subjects_page import SubjectsPage
from pages.subjects_task_page import SubjectsTaskPage
from pages.subject_information_page import SubjectInformationPage
from pages.menu_navigation_page import MenuNavigationPage
from db.db_subject_data import insert_subject_data, fetch_all_subjects
from db.db_credentials import fetch_credentials
import datetime

driver = webdriver.Chrome()
actions = ActionChains(driver)

'''
Test Requirements:
1. Navigate and login to the system.
2. Select the first subject and write the data to the database.
3. Navigate to the Admin -> Invetory Page and take a screenshot.

In the requirements, no assertions were requested. If there were, they would be here.
'''
def subject_information_test():
    CREDENTIALS = fetch_credentials()

    # Page Objects
    login_page = LoginPage(driver=driver)
    subjects_page = SubjectsPage(driver=driver)
    subjects_task_page = SubjectsTaskPage(driver=driver)
    subject_information_page = SubjectInformationPage(driver=driver)
    menu_navigation_page = MenuNavigationPage(driver=driver)

    # Requirement 1: Login
    login_page.go(CREDENTIALS['login_url'])
    login_page.login_field.input_text(CREDENTIALS['login'])
    login_page.password_field.input_text(CREDENTIALS['pw'])
    login_page.login_button.click()

    # Requirement 2: Database Population
    subjects_page.select_subject_by_index(subject_index=0)
    subjects_page.switch_windows(window_index=1)
    subjects_task_page.view_information_link.click()
    subjects_task_page.switch_windows(window_index=1)
    subject_data = subject_information_page.get_subject_data()
    insert_subject_data(subject_data)
    subject_information_page.cancel_button.click()
    subject_information_page.switch_windows(window_index=0)

    # For the convenience of the reviewers, returns the row(s) written
    db_data = fetch_all_subjects()
    for row in db_data:
        print(dict(row))

    # Requirement 3: Admin - Inventory Screenshot
    admin_menu = menu_navigation_page.admin_link
    actions.move_to_element(admin_menu.web_element).perform() # Hover over admin to reveal menu
    menu_navigation_page.admin_inventory_link.click()
    driver.save_screenshot('screenshots/{}.png'.format(str(datetime.datetime.now().timestamp())))

if __name__ == '__main__':
    subject_information_test()