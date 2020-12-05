import pytest
from TestBase.TestBase_driver import get_driver_type
from TestBase.TestBase_logger import *
from TestBase import TestBase_data

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
    #my_driver.maximize_window()

    def module_finalizer():
        logger.debug('Close browser')
        my_driver.close()
        close_logger(logger)
    request.addfinalizer(module_finalizer)


@pytest.fixture(params=TestBase_data.getTestData("Testcase1"))
def getData(request):
    return request.param


def test_DataFromExcel(getData):
    logger.info("firstname name is " + getData["firstname"])
    logger.info("lastname name is " + getData["lastname"])
    logger.info("email name is " + getData["email"])