def get_formatted_name(first_name, second_name='chen'):
    full_name = first_name + ' ' + second_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

myname = get_formatted_name('wiizard')
print(myname)


def build_person(first_name, second_name):
    person = {'first': first_name, 'second': second_name}
    return person
print(build_person('wiizard','chen'))

while True :
    print('\nPlease tell me your name:')
    f_name = input("First name:")
    s_name = input("Second name:")
    formatted_name = get_formatted_name(f_name,s_name)
    print("\nHello," + formatted_name + "!")