# Import the pytest testing framework
import pytest
# Import Selenium WebDriver to control the browser
from selenium import webdriver
# Import Service to specify Edge WebDriver path
from selenium.webdriver.edge.service import Service
# Import WebDriverWait for explicit waits
from selenium.webdriver.support.ui import WebDriverWait

# Decorator to define a pytest fixture that can be reused in tests
@pytest.fixture
def driver_setup():
    """
    # Define the fixture function named 'driver'
    """
    # Create a Service object pointing to the Edge WebDriver executable path
    service = Service(executable_path=r"C:\Users\pedrohli\PEDRO\PROGRAMAÇÃO\Projects\Selenium\app1-LearningSelenium\drivers\edgedriver_win64\msedgedriver.exe")
    # Initialize a new Edge browser instance using the configured Service
    driver = webdriver.Edge(service=service)
    # Create a WebDriverWait object to allow explicit waits up to 10 seconds
    wait = WebDriverWait(driver, 10)
    # Yield the driver and wait objects to the test function, pausing fixture here
    yield driver, wait
    # After the test finishes, quit the browser and clean up resources
    driver.quit()