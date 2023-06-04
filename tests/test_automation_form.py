import allure
from allure_commons.types import Severity

from data import users
from pages.profile_page import ProfilePage
from pages.registration_pages import RegistrationPage


@allure.tag('Web version')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Kastro')
@allure.feature('Зарегитроировать пользователя')
@allure.story('Пользователь вводит свои данные')
@allure.link('http://demoqa.com/automation-practice-form', name='demoqa')
def test_form():
    student = users.student
    registration_page = RegistrationPage()
    profile_page = ProfilePage()

    registration_page.open()
    registration_page.register(student)
    profile_page.should_have_registered(student)
