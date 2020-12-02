from selenium import webdriver
import os

# prepare path for a web driver files location / WebDriver folder /
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
web_driver_path = root_path + os.sep + 'WebDrivers' + os.sep


def get_driver_type(driver_type_from_console, _logger):
    if driver_type_from_console == "Chrome":
        _logger.info("Web driver type set by console : Chrome")
        return webdriver.Chrome(executable_path="c:/Projects/chromedriver.exe")

    elif driver_type_from_console == "Ie":
        _logger.info("Web driver type set by console : Ie")
        ie_driver_path = web_driver_path + "IEDriverServer.exe"
        return webdriver.Ie(ie_driver_path)

    elif driver_type_from_console == "Firefox":
        _logger.info("Web driver type set by console : Firefox")
        return webdriver.Firefox(executable_path=web_driver_path + "geckodriver.exe")

    elif driver_type_from_console == "None":
        '''_logger.warning("Web driver type set by default : Chrome")
        options = webdriver.ChromeOptions()  # define options
        options.add_argument("headless")  # pass headless argument to the options
        return webdriver.Chrome(executable_path="c:/Projects/chromedriver.exe", chrome_options=options)
        #return webdriver.Chrome(executable_path="c:/Projects/chromedriver.exe")'''
        _logger.info("Web driver type set by console : Chrome")
        return webdriver.Chrome(executable_path="c:/Projects/chromedriver.exe")

    else:
        _logger.warning("Web driver type set by console not known, set by default to : Firefox")
        return webdriver.Firefox(executable_path=web_driver_path + "geckodriver.exe")


def get_driver_type_nolog(driver_type_from_console):
    if driver_type_from_console == "Chrome":
        # _logger.info("Web driver type set by console : Chrome")
        return webdriver.Chrome(executable_path=web_driver_path + "chromedriver.exe")

    elif driver_type_from_console == "Ie":
        # _logger.info("Web driver type set by console : Ie")
        ie_driver_path = web_driver_path + "IEDriverServer.exe"
        return webdriver.Ie(ie_driver_path)

    elif driver_type_from_console == "Firefox":
        # _logger.info("Web driver type set by console : Firefox")
        return webdriver.Firefox(executable_path=web_driver_path + "geckodriver.exe")

    elif driver_type_from_console == "None":
        # _logger.warning("Web driver type set by default : Chrome")
        return webdriver.Chrome(executable_path=web_driver_path + "chromedriver.exe")

    else:
        # _logger.warning("Web driver type set by console not known, set by default to : Firefox")
        return webdriver.Firefox(executable_path=web_driver_path + "geckodriver.exe")
