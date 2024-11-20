import allure
from selene import browser, have


@allure.epic('Github')
@allure.feature('Github Issues')
@allure.story('Найти Issuse в репозитории')
@allure.title("Тест с декораторами")
@allure.description("поиск Issuse в репозитории с оформлением теста декораторами")
@allure.feature("Issues in repo")
@allure.tag("Issue", "Github" "Decorators")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "ParfenovaVesta")
@allure.link("https://github.com/ParfenovaVesta", name="Github")
@allure.testcase("homework_10")
def test_search_issue_in_repo_with_decorator_steps():
    open_page()

    open_repositories_list()
    open_required_repository()
    open_issues()

    should_have_issue()


@allure.step('Открываем страницу https://github.com/ParfenovaVesta')
def open_page():
    browser.open("/ParfenovaVesta")


@allure.step('Переходим в раздел репозитории')
def open_repositories_list():
    browser.element('[data-tab-item="repositories"]').click()


@allure.step('Открываем репозиторий qaguru_python_16_lesson_10')
def open_required_repository():
    browser.element("//a[@itemprop='name codeRepository']").should(have.text("qaguru_python_16_lesson_10")).click()


@allure.step('Открываем Issues')
def open_issues():
    browser.element("#issues-tab").click()


@allure.step('Проверяем наличие test_homework')
def should_have_issue():
    browser.element("#issue_1_link").should(have.text("test_homework"))
