import time
import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        # Configure Firefox Options to disable password saving prompts
        firefox_options = webdriver.FirefoxOptions()
        
        # Set preferences to block password manager and autofill prompts
        firefox_options.set_preference("signon.rememberSignons", False)
        firefox_options.set_preference("signon.autofillForms", False)
        firefox_options.set_preference("signon.generation.enabled", False)
        firefox_options.set_preference("signon.management.page.fileImport.enabled", False)
        
        driver = webdriver.Firefox(options=firefox_options)
        
    elif browser == 'edge':
        # Configure Edge Options to disable password saving prompts
        edge_options = webdriver.EdgeOptions()
        
        # Experimental preferences to disable Edge credentials service
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        edge_options.add_experimental_option("prefs", prefs)
        
        # Disable leak detection feature flag
        edge_options.add_argument("--disable-features=PasswordLeakDetection")
        
        driver = webdriver.Edge(options=edge_options)
        
    else:
        # Fallback or default browser configuration if none matches
        driver = webdriver.Firefox()

    yield driver
    time.sleep(4)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browse", default="firefox", help="Browser type: firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browse")

