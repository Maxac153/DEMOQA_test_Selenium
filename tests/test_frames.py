from pages.frames_page import FramesPage

def test_check_text_frame(driver):
    """Проверка рамки"""

    from_page = FramesPage(driver, 'https://demoqa.com/sample')
    from_page.open()
    expected_result = 'This is a sample page'
    reult_text = from_page.check_frame()
    assert expected_result == reult_text