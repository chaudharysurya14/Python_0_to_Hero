
# my_dict = {"my_name" : "Gaurav" , "my_rollno" : 7}
# my_set={5,7,89,6,6,8,'surya',}
# my_list = [1,2,3,3,3,3,3,3,3,3,3]
# my_tuple = (1,2,3,3,3,3,3,3,3)
# print(type(my_dict))
# print(type(my_list))
# print(type(my_tuple))
# print(type(my_set))
# ================================= DICT ==========================================
# my_dict={}               #for single element add in dict            #i preffer see menu driven Quistion no 2
# a=int(input('Enter a no: '))
# b=input('Enter your nam: ')
# my_dict[b]=a
# print(my_dict)

# # for multiple element add in dict
# n=int(input('How many elements wants to add in dictonary: '))
# dict1={}
# for i in range(0,n):
#     country=(input('Enter country name: '))
#     capital=(input('Enter capital name: '))
#     dict1[country]=capital
#     dict.update(dict1)
#     print(dict1)

# ===============================================================================
# =========================== LIST =====================================
# my_list=[5,3,7,2,8]                     
# a=int(input('Enter a no: '))
# my_list.append(a)                  #add element in list
# print(my_list)
# list=[]
# for p in range(0,int(input('How amny element want to add in list: '))):           #add element by range
#     list.append(input('Enter name for your list: '))
# print(list)
# ================================================================================
# ======================== SET ==========================================
# my_set=set()
# n=int(input('How many element want to add in set: '))
# for i in range(0,n):
#     elmnt=(input('Enter element for set: '))
#     my_set.add(elmnt)
# print(my_set)
# ================================================================================
# ======================== TUPLE ===========================================
my_tuple=tuple()
for i in range(0,int(input('How many element want too add in tuple: '))):
    my_tuple.update(int(input('Enter element: ')))
print(my_tuple)        