class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self) :
        print(self.name.title() + " is now siting")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('what',7)
print("My dog's name is " + my_dog.name.title() + ".") 
my_dog.sit()