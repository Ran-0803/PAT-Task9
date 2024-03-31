from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.by import By
from time import sleep

class LoginAutomation:
    """
    This method is used to login to the "https://www.saucedemo.com/" webpage using Google Chrome

    """
    def __init__(self,url="https://www.saucedemo.com/",Username="standard_user",Password="secret_sauce"):
        self.url=url
        self.username=Username
        self.password=Password
        self.driver= webdriver.Chrome(service= Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is used to start the webpage
        :return:
        """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()
    def quit(self):
        """
        This is used to close the web  browser
        :return:
        """
        self.driver.quit()


    def Login(self):
        self.boot()
        self.driver.find_element(by=By.ID,value="user-name").send_keys(self.username)
        sleep(3)
        self.driver.find_element(by=By.ID,value="password").send_keys(self.password)
        sleep(3)
        # This method is used to find login button and on it
        self.driver.find_element(by=By.ID,value="login-button").click()
        sleep(3)

        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successfully")
        else:
            print("Error")
        self.getcurrenturl()
        self.gettitle()
        self.getPagesource()
        self.quit()
    def getcurrenturl (self):
        """
        This method is used to get the current url of the webpage
        :return:
        """
        print(self.driver.current_url)
    def gettitle(self):
        """
        this method is used to get the title of the webpage
        :return:
        """
        print(self.driver.title)
    def getPagesource(self):
        """
        this method is used to get the content of the current page
        :return:
        """
        content = self.driver.page_source
        file=open("Webpage_task_11","w")
        file.write(content)
        file.close()
obj=LoginAutomation()
obj.Login()




















