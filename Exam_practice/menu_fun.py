
def show_all():
    print(my_tuple)
    print(my_set)
    print(my_list)
    print(my_dict)


def create_tuple():
    my_tuple = tuple()
    for i in range(0, int(input('How many element want too add in tuple: '))):
        my_tuple.add(int(input('Enter element for tuple: ')))
    print(my_tuple)


def create_list():
    my_list = []
    for i in range(0, int(input('How many element wants to add in list:'))):
        my_list.append(input('Enter elements:'))
    print(my_list)

def create_dict():
    my_dict = {}
    for i in range(0, int(input('How many element want to add in dict:'))):
        key = input('Enter key element for dict:')
        value = input('Enter value element for dict:')
        my_dict[key] = value
    print(my_dict)
def create_set():
    my_set = set()
    for i in range(0, int(input('How many element want to add in set'))):
        my_set.add(input('Enter element:'))
    print(my_set)

while True:
    print('======================== MENU =========================')
    print('press 1. for show all.')
    print('press 2. for create a tuple.')
    print('press 3. for create list.')
    print('press 4. for create dictonary.')
    print('press 5. for create set.')
    print('press 6. for EXIT.')
    print('=======================================================')
    choice = int(input('Enter your choice: '))
    if(choice == 1):
        show_all()
    elif(choice == 2):
        create_tuple()
    elif(choice == 3):
        create_list() 
    elif(choice == 4):
        create_dict()
    elif(choice == 5):
        create_set()
    elif(choice == 6):
        break
    else:
        print('Invalid choice,please try again!')