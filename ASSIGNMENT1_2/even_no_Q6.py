'''n=int(input('Enter a number: '))
while 0<n:
    if n%2==0:
        print(n,"is even number")
    # count=n
    n=n-1
# print(count)    


'''
'''
# ====================================================================
a=int(input('Enter a number: '))
for a in range(1,a+1):
    if a%2==0:
        print(a,"is even number")
# ====================================================================
'''
'''
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")
        
'''