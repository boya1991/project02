from Base.get_driver import get_driver
from Page.page_login import PageLogin

driver = get_driver()
class PageIn():
    def page_get_login(self):
        return PageLogin(driver)