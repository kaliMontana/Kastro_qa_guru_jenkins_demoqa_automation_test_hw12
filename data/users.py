import dataclasses


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    user_mail: str
    gender: str
    tel_number: str
    month: str
    year: str
    day: str
    first_subject: str
    second_subject: str
    hobbies: str
    upload_picture_name: str
    current_address: str
    state: str
    city: str


student = Users('Aleksandr', 'Pushkin', 'Pushkin@proton.ru', 'Male', '1234567890', 'September', '1985', '4', 'Maths',
                'Physics', 'Sports, Reading, Music', 'test_img.jpg', 'Nizhny Novgorod', 'Haryana', 'Panipat')
