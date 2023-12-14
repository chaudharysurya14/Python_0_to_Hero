import function_definitions
#print("1:       ",globals())
#print("1:       ",locals())

from function_definitions import *

#print("2:       ",globals())
#print("2:       ",locals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416
    
    def my_inner_calculator_func():
        input_num = 2 
        #global pi 
        pi = 3.14 
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("Inside one_more_inner_calculator_func pi:       ",pi)
            
            
        one_more_inner_calculator_func()
        #print("Inside my_inner_calculator_func locals:       ",locals())    
        print("Inside my_inner_calculator_func pi:       ",pi)
        
        
    #print("Inside my_iterative_calculator locals:       ",locals()) 
    my_inner_calculator_func()   
    print("Inside my_iterative_calculator pi:       ",pi)

#print("module level pi:       ",globals()[pi])    
my_iterative_calculator()
print("module level pi:       ",pi)
#print("2:       ",globals())