def geeet_users(names):
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

#usernames = ['haha', 'what', 'what your']
#geeet_users(usernames[:])   #clone one backup
#print(usernames)

def make_pizza(*toppings):
    for i in toppings:
        print(i)

#make_pizza("peperoni")
#make_pizza(1,23,4,5,6)
#make_pizza("1",'2','3')