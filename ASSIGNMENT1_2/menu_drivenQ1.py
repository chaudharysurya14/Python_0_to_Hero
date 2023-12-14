list=[]
for i in range(5):
    list.append(input('Enter name for your list: '))
print(list)
# list=['pratiksha','kevin','sachin','yuvraj','sania','surya','sneha','priyanka']
while True:
    print("1.Add member\n 2.Remove member \n 3.Display member \n 4.show number of list \n 5.for show induvidually elements in list \n 6.remove member by indexing \n 7. exit")
    choice=int(input("choose,what you want: "))
    
    if choice==0:
        print(list)
    elif choice==1:
        new_name=input('Enter name,which you want you add:')
        list.append(new_name)
        print(list)
    elif choice==2:
        newname=input('enter name which you want to remove; ')
        list.remove(newname)
        print(list) 
    elif choice==3:
        position=int(input('Enter your position: '))
        print(list[position])
    elif choice==4:
        print(len(list))
    elif choice==5:
        a=int(input('from which index you want to show: '))
        b=int(input('till where index you want to show: '))
        print(list[a:b])
    elif choice==6:
        c=int(input('which number of member you want to remove: '))
        del list[c]
        print(list)
    elif choice==7:
        break
    else: 
        print('Invalid choice,please try again!')
    '''ans=input('Do you want to continue?(y/n): ').lower()         
    if ans=='n':
        break'''
    