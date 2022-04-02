import pytest


# уровень поиска фикстур в файлах conftest
# в файле теста > в ближнем conftest

# @pytest.fixture
# def first_fixture():
#     print("\nPrint from 'first_fixture'")
#     print(">>> def first_fixture print")
# блок закомментирован, так как в файле конфтест прописана фикстура, если эту раскомментить, то будет эта отрабатывать.


def test_one(first_fixture):
    pass
    print(">>> def test_one print")

class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass
        print(">>> def test_from_test_class_one print")

    def test_from_test_class_teo(self, first_fixture):
        pass
        print(">>> def test_from_test_class_two print")