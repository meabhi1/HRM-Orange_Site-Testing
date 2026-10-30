import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from Logs.customLogger import Loggen
from selenium.common.exceptions import TimeoutException
from pages.Login import Login
from pages.AddPerson import addPerson
import os

class TestHrmOrange:
    Base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username="Admin"
    password="admin123"
    firstname="Ajay"
    middlename="Sanjay"
    lastname="Mehra"
    empId="0559"
    

    def test_login(self,setup):
        lo=Login(setup)

        logger=Loggen.logger()

        logger.info("--- Starting Test: test_login ---")
        lo.open(self.Base_url)
        logger.info(f"Navigated to Base URL: {self.Base_url}")
        
        lo.Username(self.username)
        lo.Password(self.password)
        logger.info("Entered username and password.")

        folder = "Screenshot"
        if not os.path.exists(folder):
            os.makedirs(folder)

        try:
            logger.info("Attempting to click Login button.")
            lo.LogIn()
            
            # Wait up to 10 seconds for the URL to change to the dashboard route
            WebDriverWait(setup, 10).until(EC.url_contains("dashboard"))      
            
            logger.info("Successfully navigated to the Dashboard.")
            time.sleep(2)  # Short pause to let animations settle
            setup.save_screenshot(os.path.join(folder, "test_Login_Passed.png"))
            logger.info("Saved success screenshot: test_Login_Passed.png")
        
        except TimeoutException as e:
            logger.error(f"Login failed! Timed out waiting for dashboard. Current URL: {setup.current_url}")
            
            # Save the failure snapshot immediately before raising an error
            setup.save_screenshot(os.path.join(folder, "test_Login_failed.png"))
            logger.info("Saved failure screenshot: test_Login_failed.png")
            raise e 

        
        add=addPerson(setup)

        add.click_PIM()
        add.add_btn()
        add.FirstName(self.firstname)
        add.MiddleName(self.middlename)
        add.LastName(self.lastname)
        add.save()

