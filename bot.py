# BotCity SDK
from botcity.maestro import *
from botcity.web import By

# Import necessary modules
from modules.BotManager import BotManager
from utils.helpers import click, not_found, find_and_click, find_and_type, find_elements_safe

# Load environment variables
from config.constants.enviroment_variables import BASE_URL

# Disable Maestro errors if not connected
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Maestro Integration
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID: {execution.task_id}")
    print(f"Task Parameters: {execution.parameters}")

    # ==============================
    # DESKTOP AUTOMATION EXAMPLE
    # ==============================
    desktop_bot = BotManager.get_desktop_instance()

    print("Launching desktop application...")

    desktop_bot.execute("calc.exe")
    desktop_bot.wait(2000)

    click(desktop_bot, "2_button")
    click(desktop_bot, "x_button")
    click(desktop_bot, "4_button")
    click(desktop_bot, "equals_button")

    # ==============================
    # WEB AUTOMATION EXAMPLE
    # ==============================
    webbot = BotManager.get_web_instance()

    print("Opening BotCity website...")
    webbot.browse(BASE_URL)

    input("Pressione Enter para continuar...")

    xpath_cookie = "//*[@id='hs-eu-confirmation-button']"
    find_and_click(webbot, xpath_cookie, label="Cookie button")

    xpath_login = "/html/body/div[4]/main/div[1]/div[1]/nav/div[2]/a[1]"
    find_and_click(webbot, xpath_login, label="Login button")

    webbot.wait(3000)
    webbot.stop_browser()

    # ==============================
    # FINISH TASK IN MAESTRO
    # ==============================
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Automation completed successfully."
    )

if __name__ == '__main__':
    main()
