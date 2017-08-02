#  4-10execrise
str = "The first three items in the list are:"
str_array = str.split()
print(str_array[0:4])
fullLen = str_array.__len__()
halfLen = str_array.__len__() // 2
print(str_array[halfLen:halfLen + 3])
print(str_array[fullLen-3:fullLen])
