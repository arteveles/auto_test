import pytest


@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input):
    print(test_input)

@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:

    # Все функции должны использовать аргумент
    def test_one(self, test_input):
        pass

    def test_two(self, test_input):
        pass

def test_one_1(fixture_with_params):
    print(fixture_with_params)

@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input, fixture_with_params):
    print(test_input, fixture_with_params)