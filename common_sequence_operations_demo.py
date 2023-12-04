my_string = "ICC T20 2022 WC"
my_list=['I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C']
my_tuple=('I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C')
my_range = range(1,5,1)

print("The operations in the following table are defined on Mutable/Immutable sequence types")
print("--------------------------------------------------------------------------")

print("x in s -- True if an item of s is equal to x, else False")
x= "C"
print(x in my_string)
print(x in my_list)
print(x in my_tuple)
print(1 in my_range)

print("x not in s -- False if an item of s is equal to x, else True")
x= "C"
print(x not in my_string)
print(x not in my_list)
print(x not in my_tuple)
print(1 not in my_range)

print("s+t -- 	the concatenation of s and t")
list_t= ['A','U','S','T','R','A','L','I','A']
tuple_t = ('A','U','S','T','R','A','L','I','A')
string_t = "Australia"

print(my_string + string_t)
print(my_list+list_t)
print(my_tuple+tuple_t)
# print(my_range + my_range ) # TypeError: unsupported operand type(s) for +: 'range' and 'range'

print("s * n or n * s -- 	equivalent to adding s to itself n times")
n = 2 
print(my_string * n)
print(my_list*n)
print(my_tuple*n)
#print(my_range *n ) # TypeError: unsupported operand type(s) for *: 'range' and 'range'

print("s[i] -- ith item of s, origin 0")
print(my_string[1])
print(my_list[1])
print(my_tuple[1])
print(my_range[1])

print("s[i:j] -- slice of s from i to j(Exclusive) and step 1 ")
print(my_string[1:10])
print(my_list[1:10])
print(my_tuple[1:10])
print(my_range[1:10])


print("s[i:j:k] -- 	slice of s from i to j with step k")
print(my_string[1:10:2])
print(my_list[1:10:2])
print(my_tuple[1:10:2])
print(my_range[1:10:2])


print("len(s) -- length of s")
print(len(my_string))
print(len(my_list))
print(len(my_tuple))
print(len(my_range))

print("min(s) -- smallest item of s ")
print(min(my_string))
print(min(my_list))
print(min(my_tuple))
print(min(my_range))

print(min(my_string).isspace())
print(min(my_list).isspace())
print(min(my_tuple).isspace())

print("max(s) -- smallest item of s ")
print(max(my_string))
print(max(my_list))
print(max(my_tuple))
print(max(my_range))


print("s.index(x[, i[, j]]) -- 	index of the first occurrence of x in s (at or after index i and before index j)")
print(my_string.index('C'))
print(my_list.index('C'))
print(my_tuple.index('C'))
print(my_range.index(1))

print("s.count(x) -- 	total number of occurrences of x in s")
print(my_string.count('C'))
print(my_list.count('C'))
print(my_tuple.count('C'))
print(my_range.count(1))

print("The operations in the following table are defined on mutable sequence types")
print("------------------------------------------------------------------------")

print("s[i] = x -- 	item i of s is replaced by x")
#my_string[1] = 'T'  # TypeError: 'str' object does not support item assignment 
my_list[1] =  "G"
#my_tuple[1] = "G" # TypeError: 'tuple' object does not support item assignment
#my_range[1] = 1 # TypeError: 'range' object does not support item assignment
print(my_list)

print("s[i:j] = t -- slice of s from i to j is replaced by the contents of the iterable t ");
#my_string[1:3] = ["G","A"]  # TypeError: 'str' object does not support item assignment 
my_list[1:3] =   ["G","A"]
#my_tuple[1:3]  = ["G","A"] # TypeError: 'tuple' object does not support item assignment
#my_range[1] = [1,2] # TypeError: 'range' object does not support item assignment
print(my_list)

print("del s[i:j] -- 	same as s[i:j] = []")
del my_list[1:3] 
print(my_list)

print("s[i:j:k] = t -- 	the elements of s[i:j:k] are replaced by those of t")
my_list[4:10:2] =   ["T","T","T","T"]

print("del s[i:j:k] -- 	removes the elements of s[i:j:k] from the list")
del my_list[1:6:2]
print(my_list)

print("s.append(x) -- 	appends x to the end of the sequence (same as s[len(s):len(s)] = [x])")
my_list.append("Appended String")
print(my_list)

print("s.append(x) -- 	Trying to append multiple values , did not work as anticipated ")
my_list.append(["Appended String1","Appended String2"])
print(my_list)

print("s.clear() -- removes all items from s (same as del s[:])")
my_list.clear()
print(my_list)

print("s.copy() -- creates a shallow copy of s (same as s[:])")
my_temp_list = [1,2,3,4,5,6,7,7,8,8,9]
my_list = my_temp_list.copy()
print(my_list)
print(my_temp_list)

print("s.extend(t) or s += t -- extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)")
my_list.extend(["Extended Val1","Extended Val2"])
print(my_list)
my_list += ["Extended Val3","Extended Val4"]
print(my_list)

print("s *= n -- updates s with its contents repeated n times")
my_list *= 2
print(my_list)

print( "s.insert(i, x) -- inserts x into s at the index given by i (same as s[i:i] = [x])")
my_list.insert(0,"My Inserted Val1")
print(my_list)

print( "s.insert(i, x) -- trying to add multiple elements but did not succeeded as anticipated")
my_list.insert(0,["My Inserted Val2","My Inserted Val3"])
print(my_list)

print("s.pop() or s.pop(i) -- retrieves the item at i and also removes it from s")
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)

print("s.remove(x) -- 	remove the first item from s where s[i] is equal to x")
print(my_list)
my_list.remove('Extended Val1')
print(my_list)
my_list.remove('Extended Val1')
print(my_list)

print("s.reverse() -- 	reverses the items of s in place")
print(my_list)
my_list.reverse()
print(my_list)