while True:   
    print('======================== MENU =========================')
    print('press 1. for show all.')
    print('press 2. for create a tuple.')
    print('press 3. for create list.')
    print('press 4. for create dictonary.')
    print('press 5. for create set.')
    print('press 6. for EXIT.')
    print('=======================================================')

    choice=int(input('Enter your choice: '))
    # if(choice==1):
    #     print(my_tuple)
        # print(my_set)
        # print(my_list)
        # print(my_dict)
        
    if(choice==2):
        my_tuple=tuple()
        for i in range(0,int(input('How many element want too add in tuple: '))):
            my_tuple.add(int(input('Enter element for tuple: ')))
        print(my_tuple)
        
    elif(choice==3):
        my_list=[]
        for i in range(0,int(input('How many element wants to add in list:'))):
            my_list.append(input('Enter elements:'))
        print(my_list)
        
    elif(choice==4):
        my_dict={}
        for i in range(0,int(input('How many element want to add in dict:'))):
            key=input('Enter key element for dict:')
            value=input('Enter value element for dict:')
            my_dict[key]=value
        print(my_dict)
        
    elif(choice==5):
        my_set=set()
        for i in range(0,int(input('How many element want to add in set'))):
            my_set.add(input('Enter element:'))
        print(my_set)
        
    elif(choice==6):
        break
    else: 
        print('Invalid choice,please try again!')