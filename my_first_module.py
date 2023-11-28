import builtins
""
''
""" """
''' '''

#
#begin = cut
print("Welcome to the world of Python Programming")

my_name = "gaurav"
my_rollno  = 1
my_percentage  = 1.0

my_char_string = "t"
my_dict = {"my_name" : "Gaurav" , "my_rollno" : 7}

my_list = [1,2,3,3,3,3,3,3,3,3,3]
my_tuple = (1,2,3,3,3,3,3,3,3)
my_string = "string"
my_set = {1,2,3,3,3,3,3,3,3,3}

builtins.print("Datatype of my_name reference variable is " , type(my_name))
print("My all element in the list is " , my_list )
print("My first element in the list is " , my_list[0] )

print("My all elements in the tuple is " , my_tuple )
print("My first element in the tuple is " , my_tuple[0] )

print("My all element in the string is " , my_string )
print("My first element in the string is " , my_string[0] )

print("My all element in the dictionary is " , my_dict )
print("My my_name element in the dictionary is " , my_dict["my_name"] )

print("My all element in the set is " , my_set )


#$my_first_input_var = <>;
my_first_input_var = int(input("Please provide some input number :::: "))
print(" The datatype of the value you inserted is " , type(my_first_input_var))
print(" The value you inserted is " , my_first_input_var)


MY_CONSTANT = 8
print(MY_CONSTANT)

MY_CONSTANT = 10 
print(MY_CONSTANT)


a, b, c = 5, 3.2, "Hello"
print (a)
print (b)
print (c)


(a, b, c) = (5, 3.2, "Hello")

print (a)
print (b)
print (c)


# literals

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2    # 1.5 * 10 raise to 2 

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# 

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)



# formatting in print

print("string1","string2","string3",sep = '*******' , end = '---------')
print("this is the next line ")


print("my name is " , my_name , "my_rollno is ",my_rollno)
print(f"my name is {my_name} my_rollno is {my_rollno}" )

print(f"my name is {my_name*3} my_rollno is {my_rollno}" )

str= "test"
str1= "test"

