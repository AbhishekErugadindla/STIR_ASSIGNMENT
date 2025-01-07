import os
import stat
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def setup_driver():
    chrome_options = Options()

    # Production settings for Chrome
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')

    # Handle ChromeDriver for production - Using Linux version
    CHROMEDRIVER_VERSION = "131.0.6778.204"
    CHROMEDRIVER_URL = f"https://storage.googleapis.com/chrome-for-testing-public/{CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip"
    CHROMEDRIVER_PATH = 'chromedriver/chromedriver-linux64/chromedriver'  # No .exe extension for Linux

    # Download and setup ChromeDriver
    if not os.path.exists('chromedriver'):
        try:
            os.makedirs('chromedriver', exist_ok=True)
            response = requests.get(CHROMEDRIVER_URL)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            with open('chromedriver/chromedriver.zip', 'wb') as f:
                f.write(response.content)
            
            import zipfile
            with zipfile.ZipFile('chromedriver/chromedriver.zip', 'r') as zip_ref:
                zip_ref.extractall('chromedriver')
            
            # Set executable permissions for Linux
            os.chmod(CHROMEDRIVER_PATH, stat.S_IRWXU)  # This sets read, write, and execute permissions
            
        except Exception as e:
            print(f"Error during ChromeDriver setup: {str(e)}")
            raise

    try:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error creating WebDriver: {str(e)}")
        # Print file existence and permissions for debugging
        if os.path.exists(CHROMEDRIVER_PATH):
            permissions = oct(os.stat(CHROMEDRIVER_PATH).st_mode)[-3:]
            print(f"ChromeDriver exists with permissions: {permissions}")
        else:
            print("ChromeDriver file does not exist")
        raise
