from data import users
from pages.profile_page import ProfilePage
from pages.registration_pages import RegistrationPage


def test_form():
    student = users.student
    registration_page = RegistrationPage()
    profile_page = ProfilePage()

    registration_page.open()
    registration_page.register(student)
    profile_page.should_have_registered(student)
