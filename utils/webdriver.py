# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# def setup_driver():
#     chrome_options = Options()
    
#     # Production settings for Chrome
#     chrome_options.binary_location = "/usr/bin/google-chrome"
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--disable-notifications')
#     chrome_options.add_argument('--window-size=1920,1080')

#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         return driver
#     except Exception as e:
#         print(f"Error creating WebDriver: {str(e)}")
#         raise

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import os

def setup_driver():
    # Set up Chrome options
    chrome_options = Options()
    
    # Essential arguments for running Chrome in Render
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    
    # Additional helpful arguments
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    
    # Set temporary directory for Chrome
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--user-data-dir=/opt/render/project/src/tmp')
    
    try:
        # Set up Chrome service with specific version
        chrome_version = "131.0.6778.205"  # Specify a known working version
        service = Service(ChromeDriverManager(version=chrome_version).install())
        
        # Create and return the driver
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        print("WebDriver created successfully!")
        return driver
        
    except Exception as e:
        print(f"Error creating WebDriver: {str(e)}")
        
        # Print debugging information
        print("\nDebugging Information:")
        print(f"Chrome executable path: {chrome_options.binary_location}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Directory contents: {os.listdir('.')}")
        
        if os.path.exists('/usr/bin/google-chrome'):
            print("Chrome is installed at /usr/bin/google-chrome")
            os.system('google-chrome --version')
        else:
            print("Chrome is not installed at /usr/bin/google-chrome")
        
        raise
