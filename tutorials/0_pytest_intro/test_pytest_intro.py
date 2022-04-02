# Создание тестовых файлов
"""
1) Создаеем файлы и функции с префиксом test
2) Создаем классы с префиксом Test
3) Флаг -v / -q управление подробностью вывода
4) Флаг -s позволяет отображать print`ы - ЕСЛИ БУДЕШЬ ДЕБАЖИТЬ ТЕСТЫ
5) -x / --maxfail=n Остановить тесты после 1-го или Н-го падения
6) --collect-only Собрать информацию о тестах
7) --lf запустить только последние упавшие

"""
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