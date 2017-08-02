dimensions = (200, 50)  # 元组是不允许修改的，但可以重新定义
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 100)
for value in dimensions:
    print(value)
