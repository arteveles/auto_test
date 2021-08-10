# Создание тестовых файлов
def test_one():
    print(" >>> I`m test one")

# Так же можно, но не нужно и с модулем не заработает
def test_two():
    pass
    print(" >>> test_two passed")

# Создание тестовых классов
class TestClass:

    def test_one(self):
        pass
        print(" >>> test_one in class TestClass passed")

    def test_two(self):
        pass
        print(" >>> test_two in class TestClass passed")