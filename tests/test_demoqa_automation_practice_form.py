import datetime

from qa_guru_6_10.data.users import User
from qa_guru_6_10.pages.registration_page import RegistrationPage


def test_hard(browser_size):
    registration_page = RegistrationPage()
    student = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivan@yandex.ru',
        gender='Male',
        phone_number='1234567890',
        date_of_birth=datetime.date(1992, 1, 5),
        subjects='Economics',
        hobbies='Sports',
        photo='cat.jpg',
        address='godovikova 9',
        state='NCR',
        city='Delhi'
    )
    registration_page.open_browser()
    registration_page.fill_all(student)
    registration_page.submit()
    registration_page.should_have_submited(student)
