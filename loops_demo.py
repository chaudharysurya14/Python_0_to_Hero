"""
# range(start, stop,step_size)
print(list(range(2,20,3)))
print(list(range(2,20)))
print(list(range(4))) #print(list(range(0,4)))

num=1 
while(num<10):
     print(num, end = " ")
     num+=1
     break
 
num=1 
while(num<10):
     print(num, end = " ")
     num+=1
     continue
 
num=1 
while(num<10):
     print(num, end = " ")
     continue
     num+=1



# if i want to print 1-5 but loop for 1-9
num=1 
while(num<10):
     if num<6 : 
        print(num, end = " ")
     num+=1

"""        

# prints 2-10
num=1 
while(num<10):
     if num<6 : 
        pass
     num+=1
     print(num, end = " ")
        
# ***********************************************************
# Practice problem 1 
# ***********************************************************
# Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game



