import os
from dotenv import load_dotenv

# Desktop automation
from botcity.core import DesktopBot

# Web automation
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import default_options as chrome_options
from botcity.web.browsers.firefox import default_options as firefox_options
from botcity.web.browsers.edge import default_options as edge_options

# WebDriver Manager for automatic driver download
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# Load environment variables
from config.constants.enviroment_variables import HEADLESS, BROWSER, DOWNLOAD_FOLDER

# Load environment variables
load_dotenv()

class BotManager:
    _web_instance = None
    _desktop_instance = None

    @staticmethod
    def get_web_instance():
        """
        Get or create a singleton instance of WebBot with custom browser options.
        The browser type is selected via the .env file.
        """
        if BotManager._web_instance is None:
            # Initialize WebBot instance
            BotManager._web_instance = WebBot()

            # Set headless mode based on environment variable
            BotManager._web_instance.headless = HEADLESS

            # Load browser preference from .env file
            print(f"Selected browser: {BROWSER}")

            # Download folder setup
            os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

            # Browser-specific setup
            if BROWSER == "FIREFOX":
                options = firefox_options(headless=BotManager._web_instance.headless, download_folder_path=DOWNLOAD_FOLDER)
                service = FirefoxService(GeckoDriverManager().install())
                BotManager._web_instance.driver_path = service.path
            elif BROWSER == "EDGE":
                options = edge_options(headless=BotManager._web_instance.headless, download_folder_path=DOWNLOAD_FOLDER)
                service = EdgeService(EdgeChromiumDriverManager().install())
                BotManager._web_instance.driver_path = service.path
            else:  # Default to Chrome
                options = chrome_options(headless=BotManager._web_instance.headless, download_folder_path=DOWNLOAD_FOLDER)
                service = ChromeService(ChromeDriverManager().install())
                BotManager._web_instance.driver_path = service.path

            # Apply browser options
            BotManager._web_instance.options = options

        return BotManager._web_instance

    @staticmethod
    def get_desktop_instance():
        """
        Get or create a singleton instance of DesktopBot.
        """
        if BotManager._desktop_instance is None:
            BotManager._desktop_instance = DesktopBot()
        return BotManager._desktop_instance
