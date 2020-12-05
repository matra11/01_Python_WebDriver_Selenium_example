'''import pytest
from TestBase.TestBase_driver import get_driver_type
from TestBase.TestBase_logger import *
import time

logger = None


@pytest.fixture(scope='module', autouse=True)
def module_fixture(request):

    global logger
    logger = get_logger(__name__, report_to_console=True)
    logger.debug('Start Tests module')

    def module_finalizer():
        logger.debug('End Tests module')
        close_logger(logger)

    request.addfinalizer(module_finalizer)
    return logger


@pytest.fixture(scope='module', autouse=False)
def my_driver(driver_type_from_console):

    logger.PrepStep("PrepStep open browser")
    return get_driver_type(driver_type_from_console, logger)


def test_demo(my_driver):

    logger.TestStep("TestStep test_demo to log")

    # Navigate to the application home page
    my_driver.get("http://www.google.com")

    # get the search textbox
    search_box = my_driver.find_element_by_css_selector(
        "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")

    # enter search keyword and submit
    search_box.send_keys("Selenium WebDriver Interview questions")

    # search_field.send_keys("Selenium WebDriver Interview questions")
    search_box.submit()

    logger.TestStep("TestStep end to log")


def test_demo1(my_driver):
    logger.TestStep("TestStep test_demo1 to log")
    my_driver.get("http://azet.sk")
    page_title = my_driver.title
    print("Page title = " + page_title)
    logger.TestStep("TestStep Test_1 to log")
    assert page_title == "Azet.sk - portál, kde je vždy najviac ľudí"
    #button_css ="#app > header > nav > div > div.is-logged-wrapper > div > div > span.azet-account"
    button_css ="#app > header > div > ul > li:nth-child(2) > a"
    button = my_driver.find_element_by_css_selector(button_css)
    button.click()

    #switch to new window
    window_after = my_driver.window_handles[1]
    my_driver.switch_to_window(window_after)

    page_title = my_driver.title
    print("Page title = " + page_title)
    assert page_title == "Prihlásenie"

    text_field_css = "body > div > div.landing-page__step.landing-page__step--login > div.landing-page__step_content.landing-page__step_content--login > form > div:nth-child(1) > div > input"
    text_field = my_driver.find_element_by_css_selector(text_field_css)
    text_field.send_keys("gabotest")

    text_field1_css = "body > div > div.landing-page__step.landing-page__step--login > div.landing-page__step_content.landing-page__step_content--login > form > div:nth-child(3) > div > input"
    text_field1 = my_driver.find_element_by_css_selector(text_field1_css)
    text_field1.send_keys("aaaaaa")

    button1_css ="body > div > div.landing-page__step.landing-page__step--login > div.landing-page__step_content.landing-page__step_content--login > form > input"
    button1 = my_driver.find_element_by_css_selector(button1_css)
    button1.click()

    # root > div > div.products-wrapper > div > div:nth-child(3) > div.product-action > button


def test_demo3(my_driver):
    logger.TestStep("TestStep test_demo1 to log")
    my_driver.implicitly_wait(3)

    my_driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    input_field_css= "#root > div > header > div > div.search > form > input"
    input_field = my_driver.find_element_by_css_selector(input_field_css)
    input_field.send_keys("ber")

    time.sleep(2)

    button_css = "#root > div > div.products-wrapper > div > div:nth-child(1) > div.product-action > button"
    button= my_driver.find_element_by_css_selector(button_css)
    button.click()

    time.sleep(2)

    button_css = "#root > div > div.products-wrapper > div > div:nth-child(2) > div.product-action > button"
    button = my_driver.find_element_by_css_selector(button_css)
    button.click()

    my_driver.implicitly_wait(1)
    time.sleep(2)

    button_css = "#root > div > div.products-wrapper > div > div:nth-child(3) > div.product-action > button"
    button = my_driver.find_element_by_css_selector(button_css)
    button.click()
'''
