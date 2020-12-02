import pytest
from TestBase.TestBase_driver import get_driver_type
from TestBase.TestBase_logger import *


my_driver = None
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


@pytest.fixture(scope='function', autouse=True)
def function_fixture(request, driver_type_from_console):

    logger.PrepStep('Open_browser')
    global my_driver
    my_driver = get_driver_type(driver_type_from_console, logger)
    my_driver.implicitly_wait(30)
    my_driver.maximize_window()

    def function_finalizer():
        logger.PostStep('Close_browser')
        my_driver.close()
    request.addfinalizer(function_finalizer)

    return my_driver


@pytest.mark.webtest_Azet
def test_one_one_test_1():
    my_driver.get("http://azet.sk")
    page_title = my_driver.title
    print("Page title = " + page_title)
    logger.TestStep("TestStep Test_1 to log")
    assert page_title == "Azet.sk - portál, kde je vždy najviac ľudí"


@pytest.mark.webtest_SME
def test_one_one_test_2():
    logger.TestStep("TestStep Test_2 to log")
    my_driver.get("http://sme.sk")
    page_title = my_driver.title
    print("Page title = " + page_title)
    assert page_title == "SME.sk | Najčítanejšie správy na Slovensku"




