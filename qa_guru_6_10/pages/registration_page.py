import os

from selene import be, have
from selene.support.shared import browser

from qa_guru_6_10 import resources


class RegistrationPage:

    def open_browser(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_second_name(self, second_name):
        browser.element('#lastName').type(second_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choise_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choise_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def choise_hobbies(self, hobbie):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbie)).click()

    def upload_photo(self, photo):
        browser.element('[type="file"]').send_keys(resources.path(photo))

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def choise_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def choise_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').should(be.visible).press_enter()

    def should_registered_user_with(self, full_name, email, gender, phone_number, date_of_birth, subjects, hobbies, photo, address,
                                    state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            date_of_birth,
            subjects,
            hobbies,
            photo,
            address,
            state_city
        )
    )




