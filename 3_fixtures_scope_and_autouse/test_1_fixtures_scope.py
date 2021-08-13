def test_one(first_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_one NOT in test class 1!")
    print(">>> Print test_one")

def test_two(first_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_one NOT in test class 2!")
    print(">>> Print test_two")


class TestClass:

    def test_one(self, first_fixture, class_fixture, module_fixture, session_fixture):
        print("I test_one in TestClass test class")
        print(">>> Print TestClass test_one")

    def test_two(self, first_fixture, class_fixture, module_fixture, session_fixture):
        print("I test_two in TestClass test class")
        print(">>> Print TestClass test_two")

    def test_three(self, first_fixture, class_fixture, module_fixture, session_fixture):
        print("I test_three in TestClass test class")
        print(">>> Print TestClass test_three")