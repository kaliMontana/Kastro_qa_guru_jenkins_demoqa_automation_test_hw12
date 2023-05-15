from selene import have

from data.users import Users
from pages.registration_pages import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    user = Users('Aleksandr', 'Pushkin', 'Pushkin@proton.ru', 'Male', '1234567890', 'September', '1985', '4', 'Maths',
                 'Physics', 'Sports, Reading, Music', 'test_img.jpg', 'Nizhny Novgorod', 'Haryana', 'Panipat')

    registration_page.open()

    registration_page.fill_full_name(user.first_name, user.last_name)

    registration_page.fill_email(user.user_mail)

    registration_page.choose_gender(user.gender)

    registration_page.fill_tel_number(user.tel_number)

    registration_page.fill_date_of_birth(user.month, user.year, user.day)

    registration_page.fill_subjects(user.first_subject, user.second_subject)

    registration_page.choose_hobies()

    registration_page.uplod_picture(user.upload_picture_name)

    registration_page.fill_current_address(user.current_address)

    registration_page.choose_locatio(user.state, user.city)

    registration_page.registered_user_data.should(
        have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.user_mail,
            user.gender,
            user.tel_number,
            f'0{user.day} {user.month},{user.year}',
            f'{user.first_subject}, {user.second_subject}',
            user.hobbies,
            user.upload_picture_name,
            user.current_address,
            f'{user.state} {user.city}'
        )
    )
