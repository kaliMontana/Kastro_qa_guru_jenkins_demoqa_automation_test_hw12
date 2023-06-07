import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_setup(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub/",
        options=options
    )
    browser = Browser(Config(driver=driver, base_url='https://demoqa.com/', window_width=1920, window_height=1080))

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
