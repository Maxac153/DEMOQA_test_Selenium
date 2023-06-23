from pages.check_box_page import CheckBoxPage
def test_check_box(driver):
    """Проверка флажков"""

    from_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
    from_page.open()
    result = from_page.check_path()[0]
    assert result.find('angular') and result.find('veu')