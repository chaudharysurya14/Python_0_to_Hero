
# ------------
# File handling
# -------------

# # Python program to demonstrate  opening a file
# file1 = open('my_first_file.txt',"r")
# print(file1.read())
# file1.close()

# # no need to close if we use with context
# print("Read call below \n -----------------------")

# with( open('my_first_file.txt',"r") as file1):
#     print(file1.read())

# print("Readline call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readline(),end= "---\n")

# print("Readlines call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readlines(),end= "---\n")


# print(r" strip off those \n at the end of the list ")
# with ( open('my_first_file.txt',"r") )as file1:
#     lines = []
#     for line in file1:
#         lines.append(line.strip())
# print(lines)        

# print(" Write to a file in w mode ")
# with ( open('my_first_file.txt',"w") as file1):
#     file1.write("hi there ")

# print(" Write to a file in a mode ")
# with ( open('my_first_file.txt',"a") as file1):
#     file1.write("hi there ")


# # Python program to demonstrate  opening a file in binary mode
# file1 = open('my_first_file.txt',"rb")
# print(file1.read())
# file1.close()

# # Python program to demonstrate  writing a file in binary mode
# file1 = open('my_first_file.txt',"wb")
# file1.write(b'0000000000000000000000000000000000000000000')
# file1.close()

# # Python program to demonstrate  appending a file in binary mode
# file1 = open('my_first_file.txt',"ab")
# file1.write(b'111111111111111111111111111111111111')
# file1.close()

# # Python program to demonstrate opening a binary file in text mode
# file1 = open('my_first_file.txt')
# print(file1.read())
# file1.close()


# # Key takeaways
# 1) Open / close / read / write
# 2) open modes ( r,w,a,x,r+,w+,a+)
# 3) text / binary format

# lets you know if the file handle is closed or not 
# print(file1.closed)

# # Python program to demonstrate  opening a file with some exception handling
try:
    file1 = open('my_first_file.txt',"r")
except FileNotFoundError:
    print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
    file1 = open('my_first_file.txt',"w+")
    file1.write("Default creation was done in exception block")

print(file1.read())
file1.close()
