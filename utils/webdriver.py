from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def setup_driver():
    """Setup Chrome WebDriver with production settings"""
    chrome_options = Options()

    # Production settings for Chrome
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')

    service = Service('chromedriver/chromedriver-win64')
    return webdriver.Chrome(service=service, options=chrome_options)
