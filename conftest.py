import pytest


@pytest.fixture(scope='session')
def driver_type_from_console(request):
    return request.config.getoption("--wdriver")


def pytest_addoption(parser):
    parser.addoption(
        "--wdriver", action = "store", default = "None", help = "my option: Chrome or Ie or Firefox"
    )