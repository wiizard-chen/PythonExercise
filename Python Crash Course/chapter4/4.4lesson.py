my_foods = ['eggs', 'beef', 'vegetables']
other_foods = my_foods[:]  # 返回一个数组的结果
print(my_foods)
print(other_foods)
my_foods.append('fish')
other_foods.append('chicken')
print(my_foods)
print(other_foods)

print(my_foods[0:3:3])