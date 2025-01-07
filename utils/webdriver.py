import os
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

    # Handle ChromeDriver for production
    CHROMEDRIVER_VERSION = "131.0.6778.204"
    CHROMEDRIVER_URL = f"https://storage.googleapis.com/chrome-for-testing-public/{CHROMEDRIVER_VERSION}/win64/chromedriver-win64.zip"

    # Download and setup ChromeDriver
    if not os.path.exists('chromedriver'):
        os.makedirs('chromedriver')
        response = requests.get(CHROMEDRIVER_URL)
        with open('chromedriver/chromedriver.zip', 'wb') as f:
            f.write(response.content)
        import zipfile
        with zipfile.ZipFile('chromedriver/chromedriver.zip', 'r') as zip_ref:
            zip_ref.extractall('chromedriver')

    service = Service('chromedriver/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
