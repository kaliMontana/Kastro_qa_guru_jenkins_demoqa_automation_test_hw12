import os

from selene import browser, have


def test_form():
    browser.open('/automation-practice-form')
    browser.element('.main-header').should(have.exact_text('Practice Form'))

    browser.element('#firstName').type('Aleksandr')
    browser.element('#lastName').type('Pushkin')
    browser.element('#userEmail').type('Pushkin@proton.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('1234567890')

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

    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('#subjectsInput').type('Physics').press_enter()

    for index in range(0, 3):
        browser.all('#hobbiesWrapper .custom-control-label') \
            .should(have.size_greater_than(0)) \
            .element(index).click()

    browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('..\\resources'), 'test_img.jpg'))

    browser.element('#currentAddress').type('Nizhny Novgorod')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').should(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').should(have.exact_text('Panipat')).click()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Aleksandr Pushkin',
        'Student Email Pushkin@proton.ru',
        'Gender Male',
        'Mobile 1234567890',
        'Date of Birth 04 September,1985',
        'Subjects Maths, Physics',
        'Hobbies Sports, Reading, Music',
        'Picture test_img.jpg',
        'Address Nizhny Novgorod',
        'State and City Haryana Panipat'
    ))
