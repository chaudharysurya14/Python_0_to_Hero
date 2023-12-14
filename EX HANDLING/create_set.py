print('====================MENU====================')
print('pree 1. for show your list!')
print('pree 2. for add integer element in list!')
print('pree 3. for add string in list!')
print('pree 4. for add floaating no in list!')
print('pree 5. for add tuple in list!')
print('pree 6. for add dictionary in list!')
print('pree 7. for add set in list!')
print('pree 8. for EXIT!')
print('=============================================')
num=int(input('choose your choice: '))

my_list=[]

def show_my_list():
    print(my_list)

def add_int_element():
    t=int(input('how many integer element want to add: '))
    for i in range(0,t):
        my_list.add(int(input('Enter element for list: ')))
    print(my_list)
        
def add_str_element():
    u=input('how many string element want to add: ')
    for i in range(0,u):
        my_list.add(input('Enter your string elements: '))
        print(my_list)
        
def add_floating_element():
    p=float(input('How many floating element wants to add: '))
    for i in range(0,p):        
        my_list.add(float(input('Enter floating elements: ')))
        print(my_list)
        
def add_tupl_in_list():
    q=int(input('How many elements wants to add in tuple: '))
    my_tuple=tuple()
    for i in range(0,q):
        my_tuple.add(int(input('Enter element to add in tuple: ')))
        my_list.update(my_tuple)
        print(my_list)
        
def add_dict_in_list():
    r=int(input('How many elemnents wants to add in dict: '))
    dict={}
    for i in range(0,r):
        s=input('Enter element: ')
        t=input('Enter element: ')
        dict[s]=t
        # dict.add()
        my_list.update(dict)
        print(my_list)
        
def add_set_in_list():
    t=int(input('How many element wants to in set: '))
    my_set=set()
    for i in range(0,t):
        my_set.add(input('Enter element for set: '))
        
    my_list.append(my_set) 
    print(my_list) 


while True:
    if num==1:
        show_my_list()
    
    elif num==2:
        add_int_element()
        
    elif num==3:
        add_str_element()
        
    elif num==4:
        add_floating_element()
        
    elif num==5:
        add_tupl_in_list()
        
    elif num==6:
        add_dict_in_list()
        
    elif num==7:
        add_set_in_list()
    elif num==8:
        break