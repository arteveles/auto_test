


class Test_ListComprehansion():


    nums = [1, 2, 3, 4, 5]

    # создадим список из цифр от 1 до 5, используя функцию range()
    def test_first_creation(self):
        nums = [n for n in range(1, 6)]
        print(nums)

    # каждое значение — это возведенное в квадрат значения оригинального списка
    def test_change(self):
        squares = [n*n for n in self.nums]
        print(squares)

    # вывод нечетных чисел
    def test_comprehansion_if_nechetniye(self):
        odd_squares = [n*n for n in self.nums if n%2 == 1]
        print(odd_squares)

    # вывод четных чисел
    def test_comprehansion_if_chetniye(self):
        odd_squares = [n*n for n in self.nums if n%2 == 0]
        print(odd_squares)

    #   генерация нескольких списков
    def test_comprehansion_for(self):
        matrix = [
            [x for x in range(1, 4)]
            for y in range(1, 4)
        ]
        print(matrix)

    # В этом примере мы сперва перебираем people, присваивая каждый словарь person.
    # После этого перебираем каждый идентификатор в словаре, присваивая ключи term.
    # Если значение term равно birthday, то значение person[term] добавляет в list comprehension.
    def test_practice(self):
        people = [{
            "f_n": "Василий",
            "l_n": "Васильевич",
            "brtd": "01/01/1900"
        }, {
            "f_n": "Иван",
            "l_n": "Иванович",
            "brtd": "10/10/1910"
        }]

        birthdays = [
            person[term]
            for person in people
            for term in person
            if term == "brtd"
        ]
        print(birthdays)
