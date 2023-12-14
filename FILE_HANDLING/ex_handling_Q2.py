# QUESTION 2 ================================================================================================
class posative_number_error(Exception):
    pass


def create_negative_numbered_list():
    my_list=[]
    for cntr in range(0,int(input('Please enter number of elements to the numbered list: '))):
        if (num  :=int(input("please enter number to be added: ")))>=0:
            raise  posative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# invocation
try:
    create_negative_numbered_list()        
except posative_number_error:   
    print("I handled posative_number_error exception")