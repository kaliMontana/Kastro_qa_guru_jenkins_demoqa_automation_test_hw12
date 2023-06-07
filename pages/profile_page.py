import allure
from selene import have

from data.users import Users


class ProfilePage:
    def __init__(self, browser):
        self.registered_user_data = browser.element('.table').all('td').even

    @allure.step('Проверить данны регистрации')
    def should_have_registered(self, student: Users):
        self.registered_user_data.should(
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
