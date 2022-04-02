import pytest

@pytest.fixture
def first_fixture():
    print("\nPrint from 'first_fixture'")


def test_one(first_fixture):
    pass
    print(">>> Fixture from test_one is worked")

def test_two(first_fixture):
    pass
    print(">>> Fixture from test_two is worked")

class TestFunction():

    def test_form_test_class_one(self, first_fixture):
        pass
        print(">>> Fixture from test_form_test_class_one is worked")

    def test_form_test_class_two(self, first_fixture):
        pass
        print(">>> Fixture from test_form_test_class_two is worked")