from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    # Create a Service object
    driver_path = '/home/shreya/Downloads/chromedriver/chromedriver'  # Update this path
    service = Service(executable_path=driver_path)
    
    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    
    # Provide the driver instance to the test
    yield driver
    
    # Teardown WebDriver
    driver.quit()

    