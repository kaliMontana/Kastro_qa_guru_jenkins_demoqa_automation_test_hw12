import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import users
from pages.profile_page import ProfilePage
from pages.registration_pages import RegistrationPage
from utils import attach


@allure.tag('Web version')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Kastro')
@allure.feature('Зарегитроировать пользователя')
@allure.story('Пользователь вводит свои данные')
@allure.link('http://demoqa.com/automation-practice-form', name='demoqa')
def test_form():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
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
    browser.config.driver = driver

    student = users.student
    registration_page = RegistrationPage()
    profile_page = ProfilePage()

    registration_page.open()
    registration_page.register(student)
    profile_page.should_have_registered(student)

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
