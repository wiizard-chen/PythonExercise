magicians = ['alice', 'david', 'carolina']
for person in magicians:
    print(person)
    print(person + "is a guy")

for value in range(1, 6):
    print(value)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print(min(squares))
print(max(squares))

squares_better = [value ** 2 for value in range(1,11)]  #列表解析
print(squares_better)