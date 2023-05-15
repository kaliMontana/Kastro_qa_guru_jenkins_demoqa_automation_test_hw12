from selene import have

from data.users import Users
from pages.registration_pages import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    student = Users('Aleksandr', 'Pushkin', 'Pushkin@proton.ru', 'Male', '1234567890', 'September', '1985', '4', 'Maths',
                 'Physics', 'Sports, Reading, Music', 'test_img.jpg', 'Nizhny Novgorod', 'Haryana', 'Panipat')

    registration_page.open()

    registration_page.fill_full_name(student.first_name, student.last_name)

    registration_page.fill_email(student.user_mail)

    registration_page.choose_gender(student.gender)

    registration_page.fill_tel_number(student.tel_number)

    registration_page.fill_date_of_birth(student.month, student.year, student.day)

    registration_page.fill_subjects(student.first_subject, student.second_subject)

    registration_page.choose_hobies()

    registration_page.uplod_picture(student.upload_picture_name)

    registration_page.fill_current_address(student.current_address)

    registration_page.choose_locatio(student.state, student.city)

    registration_page.registered_user_data.should(
        have.exact_texts(
            f'{student.first_name} {student.last_name}',
            student.user_mail,
            student.gender,
            student.tel_number,
            f'0{student.day} {student.month},{student.year}',
            f'{student.first_subject}, {student.second_subject}',
            student.hobbies,
            student.upload_picture_name,
            student.current_address,
            f'{student.state} {student.city}'
        )
    )
