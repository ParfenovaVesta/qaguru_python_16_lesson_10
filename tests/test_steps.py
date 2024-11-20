import allure
from selene import browser
from selene import have


def test_with_step():
    with allure.step("Открываем страницу пользователя"):
        browser.open("/ParfenovaVesta")

    with allure.step("Переходим к списку репозиториев"):
        browser.element('[data-tab-item="repositories"]').click()

    with allure.step("Открываем репозиторий"):
        browser.element("//a[@itemprop='name codeRepository']").should(have.text("qaguru_python_16_lesson_10")).click()

    with allure.step("Кликаем кнопку Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие элемента test_homework"):
        browser.element("#issue_1_link").should(have.text("test_homework"))
