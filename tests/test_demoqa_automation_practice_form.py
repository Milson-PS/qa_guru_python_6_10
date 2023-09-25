from qa_guru_6_10.pages.registration_page import RegistrationPage


def test_hard(browser_size):
    # fill form
    registration_page = RegistrationPage()
    registration_page.open_browser()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_second_name('Ivanov')
    registration_page.fill_email('ivan@yandex.ru')
    registration_page.choise_gender('Male')
    registration_page.fill_phone_number('1234567890')
    registration_page.fill_date_of_birth('1992', 'January', '05')
    registration_page.choise_subjects('economics')
    registration_page.choise_hobbies('Sports')
    registration_page.upload_photo('cat.jpg')
    registration_page.fill_address('godovikova 9')
    registration_page.choise_state('NCR')
    registration_page.choise_city('Delhi')
    registration_page.submit()

    # check form
    registration_page.should_registered_user_with('Ivan Ivanov', 'iavn@yandex.ru', 'Male', '1234567890',
                                                  '05 January,1992', 'Economics', 'Sports', 'cat.jpg', 'godovikova 9',
                                                  'NCR Delhi')
