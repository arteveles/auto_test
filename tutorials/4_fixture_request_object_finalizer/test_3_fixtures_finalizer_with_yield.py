import pytest


# реализиия финалайзера через ключевое слово yield
# но так как сделано на примере (в комментарии) ниже - понятней и прозрачней
# @pytest.fixture()
# def first_fixture_for_request(request):
#     def fin():
#         print("\nThis is finalizer from first_fixture_for_request ")
#
#     request.addfinalizer(fin)

@pytest.fixture(scope="function")
def setup_function_fixture():
    # set up - выполняется вначале
    print("\nHello from setup function fixture!\n")
    yield
    # tear down - выполняется в конце
    print("\nBye bye from setup function fixture!\n")

@pytest.fixture(scope="module")
def setup_function_fixture():
    print("\nHello from setup module fixture!\n")
    yield
    print("\nBye bye from setup module fixture!\n")

def test_one(setup_function_fixture):
    pass

def test_two(setup_function_fixture):
    pass