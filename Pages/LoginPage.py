from selenium import webdriver


class Login:
    def login_facebook(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Admin/Page_Object_Model_Final/drivers/chromedriver.exe")
        driver.get("https://www.facebook.com/")
        driver.find_element_by_id("email").send_keys("9535468206")
        driver.find_element_by_name("pass").send_keys("munisidamma@1991")
        driver.find_element_by_name("login").click()