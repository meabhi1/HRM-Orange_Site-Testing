from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

class addPerson:
    # FIX: Dynamic matching for PIM menu text regardless of whether it's active or not
    Pim_xpath = "//a[span[text()='PIM']]" 
    
    # Locators
    Add_btn_xpath = "//button[normalize-space()='Add']"
    FirstName_xpath = "//input[@placeholder='First Name']"
    MiddleName_xpath = "//input[@placeholder='Middle Name']"
    LastName_xpath = "//input[@placeholder='Last Name']"
    EmpId_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    Save_Btn = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_PIM(self):
        e = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Pim_xpath)))
        e.click()

    def add_btn(self):
        # FIX: Changed self.add_btn to self.Add_btn_xpath
        a = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Add_btn_xpath)))
        a.click()

    def FirstName(self, firstname):
        f = self.wait.until(EC.presence_of_element_located((By.XPATH, self.FirstName_xpath)))
        f.send_keys(firstname)

    def MiddleName(self, middlename):
        m = self.wait.until(EC.presence_of_element_located((By.XPATH, self.MiddleName_xpath)))
        m.send_keys(middlename)
    
    def LastName(self, lastname):
        l = self.wait.until(EC.presence_of_element_located((By.XPATH, self.LastName_xpath)))
        l.send_keys(lastname)
    
    def EmpId(self, empid):
        i = self.wait.until(EC.presence_of_element_located((By.XPATH, self.EmpId_xpath)))
        # Note: OrangeHRM auto-generates an ID; using clear() here can be finicky.
        # If it doesn't clear, use backspaces or just leave it out to accept the auto-id.
        i.clear() 
        i.send_keys(empid)   

    def save(self):
        s = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Save_Btn)))
        self.driver.execute_script("arguments[0].click()",s)
