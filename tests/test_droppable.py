from pages.droppable_page import DroppablePabe

def test_draganddrop(driver):
    """Проверка перетаскивания"""

    from_page = DroppablePabe(driver, 'https://demoqa.com/droppable')
    from_page.open()
    result = from_page.check_draganddrop()
    expected_result = 'Dropped!'
    assert expected_result == result