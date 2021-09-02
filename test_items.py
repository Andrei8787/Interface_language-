from selenium.webdriver.support.ui import WebDriverWait
def test_button_exist_(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    assert browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')