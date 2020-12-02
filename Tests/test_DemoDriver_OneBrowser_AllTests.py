import pytest
from TestBase.TestBase_driver import get_driver_type
from TestBase.TestBase_logger import *

my_driver = None
logger = None


@pytest.fixture(scope='module', autouse=True)
def module_fixture(request, driver_type_from_console):

    # initialize global logger
    global logger
    logger = get_logger(__name__, report_to_console=True)

    logger.PrepStep('Open_browser')
    global my_driver
    my_driver = get_driver_type(driver_type_from_console, logger)
    my_driver.implicitly_wait(30)
    my_driver.maximize_window()

    def module_finalizer():
        logger.debug('Close browser')
        my_driver.close()
        close_logger(logger)
    request.addfinalizer(module_finalizer)


@pytest.mark.webtest_Topky
def test_one_all_test_1():
    my_driver.get("http://topky.sk")
    page_title = my_driver.title
    print("Page title = " + page_title)
    logger.TestStep("TestStep Test_1 to log")
    assert page_title == "Topky.sk | Online spravodajstvo"


@pytest.mark.webtest_pravda
def test_one_all_test_2():
    logger.TestStep("TestStep Test_2 to log")
    my_driver.get("http://Pravda.sk")
    page_title = my_driver.title
    print("Page title = " + page_title)
    assert page_title == "Pravda.sk"


