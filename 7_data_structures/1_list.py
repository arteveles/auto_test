# список - значения хранятся под индексами, к примеру в 0 индекс можно поместить любое значение (строка 11)
# CRUD (create, remove, update, delete)

l = []
print("Type: ", type(l))

l.append(1)     # добавление значения в список
l.extend([2,3,4])
print("l ->", l)

l[0] = "One"    # в нулевой элемент списка кладем значение One
l.insert(1, 103)
print("len of l -> ", len(l))
print("l ->", l)

# Вхождение элемента в список, сколько элементов со значением 3 находится в списке
print("3 in l ->", l.count(3), "times")
print(l.pop(), l) # index or last

del l[0]    # удаление нулевого элемента из списка
# print("l -> ", l)

# Comprehension - генератор списка
# в список l складывает четные значения от 0 до 50
# l = [x for x in range(50) if x % 2 == 0]
# print(l)

# Slice