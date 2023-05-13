from selene import have

from pages.registration_pages import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_full_name('Aleksandr', 'Pushkin')

    registration_page.fill_email('Pushkin@proton.ru')

    registration_page.choose_gender('Male')

    registration_page.fill_tel_number('1234567890')

    registration_page.fill_date_of_birth('September', '1985', '4')

    registration_page.fill_subjects('Math', 'Physics')

    registration_page.choose_hobies()

    registration_page.uplod_picture('test_img.jpg')

    registration_page.fill_current_address('Nizhny Novgorod')

    registration_page.choose_locatio('Haryana', 'Panipat')

    registration_page.registered_user_data().should(
        have.exact_texts(
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
        )
    )
