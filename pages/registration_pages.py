import os

import allure
from selene import browser, have

import tests
from data.users import Users


class RegistrationPage:

    def __init__(self):
        self.main_header = browser.element('.main-header')
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_mail = browser.element('#userEmail')
        self.tel_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.month_select = browser.element('.react-datepicker__month-select')
        self.month_select_option = browser.all('.react-datepicker__month-select option')
        self.year_select = browser.element('.react-datepicker__year-select')
        self.year_select_option = browser.all('.react-datepicker__year-select option')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies_wrapper = browser.all('#hobbiesWrapper .custom-control-label')
        self.upload_pic = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.select_state = browser.element('#state')
        self.state = browser.element('#react-select-3-option-2')
        self.select_city = browser.element('#city')
        self.city = browser.element('#react-select-4-option-1')
        self.submit = browser.element('#submit')

        self.react_class = '.react-datepicker__day--outside-month'
        self.url_path = '/automation-practice-form'
        self.resource_path = '../resources/'
        self.form_title = 'Practice Form'

    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open(self.url_path)
        self.main_header.should(have.exact_text(self.form_title))

    @allure.step('ВВодить полное имя')
    def fill_full_name(self, first_name, last_name):
        self.first_name.type(first_name)
        self.last_name.type(last_name)

    @allure.step('Вводить емайл')
    def fill_email(self, email):
        self.user_mail.type(email)

    @allure.step('Вводить пол')
    def choose_gender(self, gender):
        browser.element(f'[value={gender}] + label').click()

    @allure.step('Вводить номер телефона')
    def fill_tel_number(self, number):
        self.tel_number.type(number)

    @allure.step('Вводить дату рождения')
    def fill_date_of_birth(self, month, year, day):
        self.date_of_birth_input.click()
        self.month_select.click()
        self.month_select_option \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text(month)) \
            .first.click()
        self.year_select.click()
        self.year_select_option \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text(year)) \
            .first.click()
        browser.element(f'.react-datepicker__day--00{day}') \
            .should(have.no.css_class(self.react_class)).click()

    @allure.step('Вводить предметы интереса')
    def fill_subjects(self, first_subject, second_subject):
        self.subjects_input.type(first_subject).press_enter()
        self.subjects_input.type(second_subject).press_enter()

    @allure.step('Выбирать увлечения')
    def choose_hobbies(self):
        for index in range(0, 3):
            self.hobbies_wrapper \
                .should(have.size_greater_than(0)) \
                .element(index).click()

    @allure.step('Загрузить файл')
    def upload_picture(self, file_name):
        self.upload_pic.set_value(
            os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'{self.resource_path}{file_name}')))

    @allure.step('Вводить адрес проживания')
    def fill_current_address(self, address):
        self.current_address.type(address)

    @allure.step('Выбирать место нахождения')
    def choose_location(self, state, city):
        self.select_state.click()
        self.state.should(have.exact_text(state)).click()
        self.select_city.click()
        self.city.should(have.exact_text(city)).click()
        self.submit.click()

    @allure.step('Зарегистрировать пользователя')
    def register(self, user: Users):
        self.fill_full_name(user.first_name, user.last_name)
        self.fill_email(user.user_mail)
        self.choose_gender(user.gender)
        self.fill_tel_number(user.tel_number)
        self.fill_date_of_birth(user.month, user.year, user.day)
        self.fill_subjects(user.first_subject, user.second_subject)
        self.choose_hobbies()
        self.upload_picture(user.upload_picture_name)
        self.fill_current_address(user.current_address)
        self.choose_location(user.state, user.city)
