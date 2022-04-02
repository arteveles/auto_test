import pytest


@pytest.fixture(scope="class")
def first_fixture_for_request(request):
    print("__________________")
    print(f"{request.node}")    # выведет имя функции с которой вызывается фикстура
    print(f"{request.scope}")   # выведет имя скоупа, который указан в @pytest.fixture(scope="class")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("__________________")
    # print("\nRequest object data: ")
    # for el in list(dir(request)):
    #     print(el)                         # покажет какие еще плагины можно использовать помимо scope="class"


def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")

class TestClass:

    def test_two(self, first_fixture_for_request):
        print("\nPrint from 'test_two'")

    def test_three(self, first_fixture_for_request):
        print("\nPrint from 'test_three'")