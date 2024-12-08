class BasePage(object):
    '''
    The Base Page object handles functions that can be shared with all page objects.
    '''
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)
    
    def switch_windows(self, window_index):
        new_window = self.driver.window_handles[window_index]
        self.driver.switch_to.window(new_window)
