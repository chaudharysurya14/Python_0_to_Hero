# my_set = {1,2,3,43,4,5,5,6,7,7,7,8,8,8,8,"gaurav","Pune",("dbda,hpcsa","diot","dac"),frozenset({"dbda,hpcsa","diot","dac"})}

'''# QUESTION NO 1 ====================================================================================================================
print(len(my_set)) 

# QUESTION NO 2 =============================================================================================================
my_set2={5,6,7}   #this search only exact match
print(my_set2 in my_set)

# QUESTION NO 3 =========================================================================================
my_set2={5,6,7}
print(my_set2 not in my_set)

# DISJOINT    =================================================
my_set2='pune'
print(my_set.isdisjoint(my_set2))

# SUBSET   =================================================
my_set2='pune'
print(my_set.issubset(my_set2))

# set  =================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set2 < my_set)
print(my_set3 <= my_set)


#  SUPERSET =========================================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set > my_set2)
print(my_set >= my_set3)


# UNION ===================================================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set | my_set2)


# INTERSECTION ================================================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set2 & my_set)
print(my_set3 & my_set)

# DIFFRENCE ============================================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set2 - my_set)
print(my_set3 - my_set)

# SYMMETRIC DIFFRENCE =============================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
print(my_set2 ^ my_set)
print(my_set3 ^ my_set)


my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
my_set4=my_set3.copy()
# print(my_set2 copy(my_set))
print(my_set4)



#  UPDATE ========================================================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {9,10,11}
# my_set3 = {("dbda,hpcsa", "diot", "dac")}
my_set2.update(my_set)
print(my_set2)
'''

# INTERSECTION UPDATE ==============================================================
my_set = {1, 2, 3, 43, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, "gaurav", "Pune",("dbda,hpcsa", "diot", "dac"), frozenset({"dbda,hpcsa", "diot", "dac"})}
my_set2 = {1, 2, 3}
my_set3 = {("dbda,hpcsa", "diot", "dac")}
# print(my_set2 &= my_set





