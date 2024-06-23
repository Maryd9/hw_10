import allure
from selene import by, be, browser
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step("Открываем главную страницу"):
        browser.open('/')

    with allure.step("Ищем репозиторий"):
        s('.search-input').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие issue с номером 76"):
        s(by.partial_text('#76')).should(be.visible)
