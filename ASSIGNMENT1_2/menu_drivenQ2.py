n=int(input('How many elements do you want in dictonary: '))
dict={}
for i in range(0,n):
    country=(input('Enter country name: '))
    capital=(input('Enter capital name: '))
    dict[country]=capital
def view_dict():
    print(dict) 
      
def dict_len():
    print("No of elements in dictionary: ",len(dict))
   
    
def dict_add():
    country=(input('Enter country name: '))
    capital=(input('Enter capital name: '))
    dict[country]=capital
    print(dict)
    
def dict_update():
    n=int(input('How many elements wants to add in dictonary: '))
    dict1={}
    for i in range(0,n):
        country=(input('Enter country name: '))
        capital=(input('Enter capital name: '))
        dict1[country]=capital
        dict.update(dict1)
        print(dict)
def dict_remove():
    country=(input('Enter country name: '))
    dict.pop(country)
    print(dict)

print("====================MENU==============================")
print("Following Options are available")
print("Press '1' for display the dictionary!")
print("Press '2' for display number of elements in dictionary!")
print("Press '3' for add one country and their capital in dictionary!")
print("Press '4' for add multiple country and their capitals in dictionary!")
print("Press '5' for remove any country from list! ")
print("Press '6' for exit: ")
print("========================================================================")


while True:
    choice=int(input("Choose your choice: "))
    if choice==1:
        view_dict()
    elif choice==2:
        dict_len()
    elif choice==3:
        dict_add()
    elif choice==4:
        dict_update()
    elif choice==5:
        dict_remove()
    elif choice==6:
        break
    else: 
        print('Invalid choice,please try again!')




'''
if choice==0:
            print(dict)
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
            
            



n=int(input('How many elements do you want in dictonary: '))
dict={}
for i in range(0,n):
    country=(input('Enter country name: '))
    capital=(input('Enter capital name: '))
    dict[country]=capital
    print(dict)
    
    
    
    
dict={"India" : "New Delhi",
"USA" : "Washington DC",
"Nepal": "Kathmandu",
"Ukraine" : "Kyiv"}
'''