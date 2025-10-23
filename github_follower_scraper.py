from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def SignIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.ID, "login_field").send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element(By.NAME, "commit").click()
        self.browser.maximize_window()
        time.sleep(20)

    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")

        for item in items:
            usernames = item.find_elements(By.CSS_SELECTOR, ".link-gray.pl-1")
            for username in usernames:
                self.followers.append(username.text)

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        self.loadFollowers()

        while True:
            btn_group_elements = self.browser.find_elements(By.CLASS_NAME, "BtnGroup")
            if btn_group_elements:
                links = btn_group_elements[0].find_elements(By.TAG_NAME, "a")
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click()
                            time.sleep(1)
                            self.loadFollowers()
                        else:
                            continue
            else:
                break

username="muratkazma0"
password=":)"
github = Github(username, password)
github.SignIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
