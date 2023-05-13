import os

from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.main-header').should(have.exact_text('Practice Form'))

    def fill_full_name(self, firstName, lastName):
        browser.element('#firstName').type(firstName)
        browser.element('#lastName').type(lastName)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self, gender):
        browser.element(f'[value={gender}] + label').click()

    def fill_tel_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option') \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text(month)).first.click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option') \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text(year)).first.click()
        browser.element(f'.react-datepicker__day--00{day}') \
            .should(have.no.css_class('.react-datepicker__day--outside-month')).click()

    def fill_subjects(self, first_subject, second_subject):
        browser.element('#subjectsInput').type(first_subject).press_enter()
        browser.element('#subjectsInput').type(second_subject).press_enter()

    def choose_hobies(self):
        for index in range(0, 3):
            browser.all('#hobbiesWrapper .custom-control-label') \
                .should(have.size_greater_than(0)) \
                .element(index).click()

    def uplod_picture(self, file_name):
        browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('..\\resources'), file_name))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_locatio(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').should(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').should(have.exact_text(city)).click()
        browser.element('#submit').click()

    def registered_user_data(self):
        browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
        return browser.element('.table').all('td').even
