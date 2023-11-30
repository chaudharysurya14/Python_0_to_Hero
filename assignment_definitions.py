
def list_display_members(members):
    """Display number of elements in the members list"""
    print("Members list = ",end = " ")
    for elem in members:
        print(elem,end= " ")

def list_add_element(members):
    """Add "Ross" to the members collection """
    members.append(input("Please input an element to add to the existing list "))
    list_display_members(members)

def list_add_elements(members):
    """Add "David","Bret","Sanju"  to the members collection"""    
    received_str = input("Please input elements comma seperated to add to the existing list ")
    members.extend(received_str.split(","))
    list_display_members(members)

def list_remove_element(members):
    """  Remove the third member from the collection"""    
    members.pop(int(input("Please enter the subscript you would want to remove element from")))
    list_display_members(members)

def remove_last_element(members):
    """Remove the last member from the collection """
    members.pop()
    list_display_members(members)    

def display_3_4_5_element(members):
    """Display third, fourth and fifth element from the collection """    
    print(members[2]+ " " + members[3]+ " " + members[4])    
    list_display_members(members)    

def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    members = input('for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] \n').split(",")

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
    
def dict_display_capitals(capitals):
    """Display number of elements in the capitals collection"""
    print("capitals dictionary = ",end = " ")
    for elem in capitals.items():
        print(elem,end= " ")

def dict_add_element(capitals):
    """Add "Afghanistan": "Kabul"  to the capitals collection """
    inp_key = input("Please enter the key to add ")
    inp_val = input("Please enter the value to add ")
    capitals.setdefault(inp_key,inp_val)
    dict_display_capitals(capitals)		

def dict_add_elements(capitals):
    """Add Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella to the capitals collection"""    
    """ Logic : 
    1) "key1":"val1","key2":"val2"

        2) 
        "key1":"val1" ==> list("key1", "val1") ==> capitals("key1") = "val1"
        "key2":"val2" ==> list("key2", "val2") ==>  capitals("key2") = "val2"
    """
    received_str = input("Please input dictinary elements comma seperated to add ")

    for dict_elem in received_str.split(","):
        temp_list = list(dict_elem.split(":"))
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()
    dict_display_capitals(capitals)		
	
def dict_remove_element(capitals):
    """Remove the USA from the collection"""    
    capitals.pop(input("Please enter the key you would want to remove"))
    dict_display_capitals(capitals)		

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    capitals= {}
    for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        temp_list = dict_elem.split(":")
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")	
            
def set_union(setA,setB):
  set_display(setA)
  set_display(setB)
  print("Union",setA.union(setB))

def set_intersection(setA,setB):
  set_display(setA)
  set_display(setB)
  print("Intersection",setA.intersection(setB))  

def set_minus(setA,setB):
  set_display(setA)
  set_display(setB)
  print("Difference",setA.difference(setB))    

def is_member_of_set(rcv_set):
   element= input("Please enter element to search for ") 
   print(f"Element{element} is present(True/False): { element in rcv_set }")  
   set_display(rcv_set)

def set_display(rcv_set):
   print(rcv_set)

def set_add_element(rcv_set):
	rcv_set.add(input("Please enter element to add"))   
	set_display(rcv_set)
	
def set_add_elements(rcv_set):
    for set_elem in input("Please enter comma seperated elements for the set ").split(","):
        rcv_set.add(set_elem.strip())   
    set_display(rcv_set)
	
def set_remove_element(rcv_set):
    rcv_set.discard(input("Please enter element to remove"))
    set_display(rcv_set)            


def my_set_store():
    print("\n Welcome to Our Set Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    setA= set()
    setB= set()

    for set_elem in input("Please enter comma seperated elements for the set A").split(","):
        setA.add(set_elem.strip())   

    for set_elem in input("Please enter comma seperated elements for the set B").split(","):
        setB.add(set_elem.strip())   


    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")

        choice = int(input("Please enter your choice "))

        if choice   ==1:
            set_union(setA,setB) 
        elif choice ==2:
            set_intersection(setA,setB)
        elif choice ==3:
            set_minus(setA,setB)
        elif choice ==4:
            set_minus(setB,setA)
        elif choice ==5:
            is_member_of_set(setB) 
        elif choice ==6:
            set_display(setA)
        elif choice ==7:
            set_display(setB)
        elif choice ==8:
            set_add_element(setA)
        elif choice ==9:
            set_add_elements(setA)
        elif choice ==10:
            set_remove_element(setA)
        elif choice ==11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")    

"""
Incomplete solution 
4) Take a number from the user and print fibonacci sequence till that number USING Range function 
	eg : fibonnaci sequence for 5 is 1,2,3,5 
"""

# def fibonacci_range():
#     upto_num = int(input("Please enter a number upto which you want Fibonnaci sequence"))            
#     n1= -1
#     n2 = 1
#     for i in range(0,upto_num+3):
#         if n1>= upto_num:
#             break
#         sum = n1+n2
#         print(sum)
#         n1=n2
#         n2=sum

