# B= {1,2,3,4,5,'hpcap','hpcsa',}
# set4 = [18,19,20,21]
n=int(input('How many element wants you in set: '))
set1=set()

for i in range(n):
    inp=input('Enter elements for create set1: ')
    set1.add(inp)
    
    print(set1)
    

n=int(input('How many element wants you in set: '))
set2=set()

for i in range(n):
    inpu=input('Enter elements for create set1: ')
    set2.add(inpu)
    
    print(set2)
    
    
def union():
    print("A union B:", set1.union(set2))
    
    print(set1)
    print(set2)

    
def intersection():
    print("A intersection B:", set1.intersection(set2))
    
    print(set1)
    print(set2)
    
    
def A_subtract_B():
    print("A - B:", set1 - set2)
    
    print(set1)
    print(set2)
    
    
def B_subtract_A():
    print("B - A:", set2 - set1)
    
    print(set1)
    print(set2)
    
    
def check_in_b():
    x=input('Enter element for A: ')
    print(x in set2)
    
    print(set1)
    print(set2)
    
    
def display_set1():
    print('elements of set1:' , len(set1))
    
    print(set1)
    print(set2)
    
    
def add_no():
    h=int(input('Enter a number: '))
    set1.add(h)
    
    print(set1)
    print(set2)


def add_no_in_B():
    n=int(input('How many element wants you add into the temp set: '))
    temp_set=set()
    
    for i in range(n):
        inp=input('Enter elements for temp set: ')
        temp_set.add(inp)      
    set1.update(temp_set)    

    print(set1)
    print(set2)
    
def remove():
    rem=input('Enter element which you want to remove: ')
    set2.remove(rem)

    print(set1)
    print(set2)


    
print("====================MENU==============================")
print("Following Options are available")
print("Press '1' for display A union B:")
print("Press '2' for display A intersection B:")
print("Press '3' for display A-B:")
print("Press '4' for display B-A:")
print("Press '5' for Display if that element is a member of set B which inserted by user:")
print("Press '6' for Display number of elements in the set A:")
print("Press '7' for Add any element in set1:")
print("Press '8' for add multiole element in set2:")
print("Press '9' for remove any element in set2:")
print("Press '10' for EXIT:")
print("========================================================================")


while True:
    choice=int(input("Choose your choice: "))
    if choice==1:
        union()

    elif choice==2:
        intersection()

    elif choice==3:
        A_subtract_B()

    elif choice==4:
        B_subtract_A()

    elif choice==5:
        check_in_b()

    elif choice==6:
        display_set1()

    elif choice==7:
        add_no()

    elif choice==8:
        add_no_in_B()

    elif choice==9:
        remove()

    elif choice==10:
        break

    else: 
        print('Invalid choice,please try again!')
