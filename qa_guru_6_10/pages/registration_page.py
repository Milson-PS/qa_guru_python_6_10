from selene import be, have
from selene.support.shared import browser

from qa_guru_6_10 import resources
from qa_guru_6_10.data.users import User


class RegistrationPage:

    def fill_all(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choise_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.choise_subjects(user.subjects)
        self.choise_hobbies(user.hobbies)
        self.upload_photo(user.photo)
        self.fill_address(user.address)
        self.choise_state(user.state)
        self.choise_city(user.city)

    def open_browser(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choise_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="' + str(month) + '"]').click()
        browser.element(f'.react-datepicker__day--0{day}').should(be.clickable).click()

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

    def should_have_submited(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.date_of_birth.strftime("%d %B,%Y"),
            user.subjects,
            user.hobbies,
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        )
        )
