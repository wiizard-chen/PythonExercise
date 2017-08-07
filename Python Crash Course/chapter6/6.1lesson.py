# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# array = []
# array.append(1)
# array.append(2)
# print(array)

# dic0 = {}
# dic0['test1'] = 2
# dic0['test2'] = 3
# for key in dic0.keys():
#     print(dic0[key])

# for key in dic0:
#     print(dic0[key])


# for key, value in dic0.items():
#     print(key + str(value))

favorite_languages = {'jen': 'python',    'sarah': 'c',
                      'edward': 'ruby',    'phil': 'python', }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

for i in pizza.values():
    print(i)