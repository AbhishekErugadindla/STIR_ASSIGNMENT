import os
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

    # Additional settings for Render
    chrome_options.binary_location = os.getenv("CHROME_BINARY_LOCATION", "/usr/bin/google-chrome-stable")

    # Use ChromeDriver from PATH
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver