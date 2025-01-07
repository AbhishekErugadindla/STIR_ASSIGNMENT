# utils/webdriver.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import platform
import subprocess
import os
import logging

logger = logging.getLogger(__name__)


def setup_driver():
    """Setup Chrome WebDriver with platform-agnostic settings"""
    chrome_options = Options()

    # Common options for all environments
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--disable-extensions')

    # Check if running on Render or other cloud platform
    if os.environ.get('RENDER') or os.environ.get('DEPLOYMENT_PLATFORM'):
        try:
            # Install Chrome and ChromeDriver on Linux
            logger.info("Setting up Chrome and ChromeDriver for cloud environment...")
            subprocess.run(['apt-get', 'update'], check=True)
            subprocess.run(['apt-get', 'install', '-y', 'chromium', 'chromium-driver'], check=True)

            chrome_options.binary_location = '/usr/bin/chromium'
            return webdriver.Chrome(options=chrome_options)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install browser dependencies: {e}")
            raise
        except Exception as e:
            logger.error(f"Error setting up cloud browser: {e}")
            raise
    else:
        # Local development setup based on OS
        try:
            system = platform.system().lower()
            logger.info(f"Setting up ChromeDriver for {system}")

            if system == 'windows':
                driver_path = 'chromedriver/chromedriver-win64/chromedriver.exe'
            elif system == 'darwin':  # macOS
                driver_path = 'chromedriver/chromedriver-mac64/chromedriver'
            else:  # Linux
                driver_path = 'chromedriver/chromedriver-linux64/chromedriver'

            if not os.path.exists(driver_path):
                logger.error(f"ChromeDriver not found at {driver_path}")
                raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

            service = Service(driver_path)
            return webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:
            logger.error(f"Error setting up local browser: {e}")
            raise
