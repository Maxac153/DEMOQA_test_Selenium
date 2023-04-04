from pages.form_page import FormPage

def test_form(driver):
    """Проверка формы"""

    form_page = FormPage(driver, 'https://demoqa.com/text-box')
    form_page.open()

    first_name, last_name, email = form_page.fill_fields_and_submit()
    result = form_page.form_result()
    assert f'{first_name} {last_name}' == result[0]
    assert email == result[1]