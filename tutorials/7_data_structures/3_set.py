# множество без повторений, пригождается для проверки уникальных элементов, не упорядоченная

s = set()

s.add('1')
s.add('2')
s.add('3')
s.add('1')
s.add('1')

print(s)
print('pop el ->', s.pop())
print('len ->', len(s))

# Для чего используют?
s1 = {1,2,3,4}
s2 = {3,4,5,6}
# 1) Поиск пересечений
print(s1.intersection(s2))
# 2) Поиск различий
print(s1.difference(s2))
print(s2.difference(s1))
