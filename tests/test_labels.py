import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link('', name="Testing")


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "masha")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link('', name="Testing")
def test_decorator_labels():
    pass
