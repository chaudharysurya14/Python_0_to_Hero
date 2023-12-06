# variable scope demonstration 
from function_definitions import *

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416
    some_list = [1,2,3,4]
    
    def my_inner_calculator_func():
        input_num = 2 
        #global pi #nonlocal pi
        pi = 3.14
        some_list = [5,6,7,8]
        #some_list[1] = 100
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            some_list = [9,10,11,12]
            #some_list[2] = 100000
            print("Inside one_more_inner_calculator_func pi:       ",pi)
            print("Inside one_more_inner_calculator_func somelist[]   :       ",some_list)
            
        one_more_inner_calculator_func()
        print("Inside my_inner_calculator_func pi:       ",pi)
        print("Inside my_inner_calculator_func somelist[]   :       ",some_list)

    my_inner_calculator_func()   
    print("Inside my_iterative_calculator pi:       ",pi)
    print("Inside my_iterative_calculator somelist[]   :       ",some_list)


my_iterative_calculator()
print("module level pi:       ",pi)

"""
#######*************************** Key Takeaways ************************* ######
##### for immutable values ot works as pass by values but for immmutable datatypes it works as pass by reference if inplace modification is done 
##### even when we dont use local/ global keyword 
##### we use local/ global keywords to somewhat have that pass by reference simulation when the variable names in a scope clashes and the local scope takes precedence

# complete replacement of list (works like pass by value when not used any local/global keyword )

Inside one_more_inner_calculator_func somelist[]   :        [9, 10, 11, 12]
Inside my_inner_calculator_func somelist[]         :        [5, 6, 7, 8]
Inside my_iterative_calculator somelist[]          :        [1, 2, 3, 4]

# in place modification of list (works like pass by reference as good as saying we are using nonlocal keyword when not used any local/global keyword )

Inside one_more_inner_calculator_func somelist[]   :  [1, 100, 100000, 4]
Inside my_inner_calculator_func somelist[]         :  [1, 100, 100000, 4]
Inside my_iterative_calculator somelist[]          :  [1, 100, 100000, 4]

"""

###### globals() and locals() demonstration below #######
# globals at any point gives you global definitions
import function_definitions
print("1:       ",globals())

from function_definitions import *
print("2:       ",globals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416
    
    def my_inner_calculator_func():
        input_num = 2 
        pi = 3.14
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("3:       ",globals())
            
        one_more_inner_calculator_func()
        print("4:       ",globals())
          
    my_inner_calculator_func()   
    print("5:       ",globals())

my_iterative_calculator()


# locals at any point gives you local definitions
import function_definitions
print("1:       ",locals())

from function_definitions import *

print("2:       ",locals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416

    def my_inner_calculator_func():
        input_num = 2 
        pi = 3.14
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("3:       ",locals())
            
        one_more_inner_calculator_func()
        print("4:       ",locals())
          
    my_inner_calculator_func()   
    print("5:       ",locals())

my_iterative_calculator()

    
    
    

