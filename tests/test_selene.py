from selene import browser
from selene import have


def test_with_selene():
    browser.open("/ParfenovaVesta")
    browser.element('[data-tab-item="repositories"]').click()
    browser.element("//a[@itemprop='name codeRepository']").should(have.text("qaguru_python_16_lesson_10")).click()
    browser.element("#issues-tab").click()
    browser.element("#issue_1_link").should(have.text("test_homework"))
