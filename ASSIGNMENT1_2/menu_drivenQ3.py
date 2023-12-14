# ============================FIBONACCI SERIES ==============================
n1=0
n2=1
# count=0
def case0():
    print("not possible fibonacci series of 0 !")

def case1():
    print("Fibonacci series of ",num,":")
    print(n1)
   
def nterm(): 
    print("Fibonacci sequence:")
    count=0
    global n1,n2
    while count < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

while True:
    num = int(input("How many terms? "))
    if num==0:
        case0()
    elif num==1:
        case1()
    elif num>1:
        nterm()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
''' 
num = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

if num<= 0:
   print("not possible febonanci series of 0 !")

elif num == 1:
   print("Fibonacci series of ",num,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
     
       n1 = n2
       n2 = nth
       count += 1'''