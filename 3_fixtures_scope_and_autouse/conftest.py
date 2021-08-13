import pytest

@pytest.fixture()
def function_fixture(request):
    print(f"\nHello from {request.scope} fixture!")

    def fin():
        print(f"\nFinalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\nHello from {request.scope} fixture!")


    def fin():
        print(f"\nFinalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\nHello from {request.scope} fixture!")


    def fin():
        print(f"\nFinalize from {request.scope} fixture!")


    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\nSession from {request.scope} fixture!")


    def fin():
        print(f"\nFinalize from {request.scope} fixture!")


    request.addfinalizer(fin)


# @pytest.fixture(autouse="True") # вызываться будет на уровне функций тестов, находящихся в той же папке с файлом conftest
# @pytest.fixture(autouse="True", scope="session") # вызываться будет в начале теста (раз в сессию), находящихся в той же папке с файлом conftest
# @pytest.fixture(autouse="True", scope="module")
@pytest.fixture(autouse="True", scope="class")
def always_used_fixture():
    print(f"\n Hello, i`m fixture with autouse and function scope used only")

