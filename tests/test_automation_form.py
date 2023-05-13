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

    def fill_tel_number(self):
        browser.element('#userNumber').type('1234567890')

    def fill_birthdate(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option') \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text('September')).first.click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option') \
            .should(have.size_greater_than(0)) \
            .filtered_by(have.exact_text('1985')).first.click()
        browser.element('.react-datepicker__day--004') \
            .should(have.no.css_class('.react-datepicker__day--outside-month')).click()

    def fill_subjects(self):
        browser.element('#subjectsInput').type('Math').press_enter()
        browser.element('#subjectsInput').type('Physics').press_enter()

    def choose_hobies(self):
        for index in range(0, 3):
            browser.all('#hobbiesWrapper .custom-control-label') \
                .should(have.size_greater_than(0)) \
                .element(index).click()

    def uplod_picture(self):
        browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('..\\resources'), 'test_img.jpg'))

    def fill_current_address(self):
        browser.element('#currentAddress').type('Nizhny Novgorod')

    def choose_locatio(self):
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').should(have.exact_text('Haryana')).click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').should(have.exact_text('Panipat')).click()
        browser.element('#submit').click()

    def should_registered_user_whith(self):
        browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(
            'Aleksandr Pushkin',
            'Pushkin@proton.ru',
            'Male',
            '1234567890',
            '04 September,1985',
            'Maths, Physics',
            'Sports, Reading, Music',
            'test_img.jpg',
            'Nizhny Novgorod',
            'Haryana Panipat'
        ))


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_full_name('Aleksandr', 'Pushkin')

    registration_page.fill_email('Pushkin@proton.ru')

    registration_page.choose_gender('Male')

    registration_page.fill_tel_number()

    registration_page.fill_birthdate()

    registration_page.fill_subjects()

    registration_page.choose_hobies()

    registration_page.uplod_picture()

    registration_page.fill_current_address()

    registration_page.choose_locatio()

    registration_page.should_registered_user_whith()
