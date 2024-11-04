from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class DeleteTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        # set username and password
        self.username = kwargs["username"] if "username" in kwargs.keys() else
        self.password = kwargs["password"] if "password" in kwargs.keys() else

    def test_website(self, *args, **kwargs):
        driver = self.driver
        driver.get("https://deltanew.ir")
        driver.maximize_window()

        driver.find_element(By.PARTIAL_LINK_TEXT, "کاربری").click()
        driver.find_element(By.ID, "txtSenderName").send_keys(self.username + Keys.ENTER)
        driver.find_element(By.ID, "txtpass").send_keys(self.password + Keys.ENTER)


        driver.find_element(By.XPATH ,"//*[text() ='املاک بررسی نشده']").click()
        driver.find_element(By.ID ,"btnSearch").click()

        sleep(3)
        # btn = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH ,"//*[contains( text(),'تست' )]/..//td[11]" )))
        btns = driver.find_elements(By.XPATH, "//*[contains( text(),'تست' )]")

        # deleted manual
        deleted = 0
        i=len(btns)
    try:
        while i > 0:
            btn = driver.find_element(By.XPATH, "//*[contains( text(),'تست' )]/..//td[12]/*")
            actions = ActionChains(driver)
            actions.move_to_element(btn)
            actions.click(btn)
            sleep(1)
            actions.perform()
            sleep(2)
            btn_delete = driver.find_element(By.XPATH, "//*[@title = 'حذف']").click()
            sleep(2)
            other_reason = driver.find_element(By.XPATH, "//label[text()='سایر موارد']").click()
            sleep(2)
            btn_delete_complite = driver.find_element(By.XPATH, "//*[@id = 'OkDepositDiv']").click()
            sleep(2)
            btns = driver.find_elements(By.XPATH, "//*[contains( text(),'تست' )]")
            i=len(btns)
            sleep(3)
    except:
        print("if you see this message, you dont have any test product Or have error in proccess")


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

