from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 

from selenium.webdriver.support import expected_conditions as EC

class Login:
    username_xpath="//input[@placeholder='Username']"
    password_xpath="//input[@placeholder='Password']"
    login_btn="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    def open(self,url):
        self.driver.get(url)


    def Username(self,username):
        user=self.wait.until(EC.presence_of_element_located((By.XPATH,self.username_xpath)))
        user.clear()
        #user=self.driver.find_element(By.XPATH,self.username_xpath).clear()
        user.send_keys(username)

    def Password(self,password):
         pas=self.wait.until(EC.presence_of_element_located((By.XPATH,self.password_xpath)))
         pas.clear()
         #pas=self.driver.find_element(By.XPATH,self.password_xpath).clear()
         pas.send_keys(password)

    def LogIn(self):
        btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,self.login_btn)))
        #btn=self.driver.find_element|(By.XPATH,self.login_btn)
        self.driver.execute_script("arguments[0].click()",btn)
