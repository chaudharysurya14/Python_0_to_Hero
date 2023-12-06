print("Changed in version 3.7: Dictionary order is guaranteed to be insertion order. ")
print("""Please do not rely on the insertion order for dictionary since it is newly introduced
      older implementation were not backported hence your same code may fail if you are on
      running it on version <3.7 and rely on insertion order for any logic of any kind
      """)

my_dict = {"name": "gaurav", "rollno": 1 , "city": "Pune","Subjects" : ["DBDA","DIOT","DAC","HPCSA"]}

print(my_dict)
print("list(d) -- Return a list of all the keys used in the dictionary d.")
print(my_dict.keys()) # dict_keys(['name', 'rollno', 'city', 'Subjects'])
print(list(my_dict))


print("len(d) --Return the number of items in the dictionary d.")
print(len(my_dict))

print("d[key] --Return the item of d with key key. Raises a KeyError if key is not in the map");
print(my_dict["name"])
#print(my_dict["name1"]) #KeyError: 'name1'

print("""
      get(key[, default])
        Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to None, so that this method never raises a KeyError.
      """)
print(my_dict.get("name"))
print(my_dict.get("name1"))
print(my_dict.get("name1","Default_value"))

print("d[key] = value --Set d[key] to value.")
my_dict["name"] = "Testing"
print(my_dict)
my_dict["name1"] = "new_field_value"
print(my_dict)

print("del d[key] -- Remove d[key] from d. Raises a KeyError if key is not in the map.")
del my_dict["name1"]
print(my_dict)
#del my_dict["name1"] # KeyError: 'name1'

print("key in d -- Return True if d has a key key, else False.")
print("name" in my_dict)
print("name1" in my_dict)

print("key not in d -- Equivalent to not key in d.")
print("name" not in my_dict)
print("name1" not in my_dict)

print( " iter(d) --Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).")
print(iter(my_dict))

print("clear() -- Remove all items from the dictionary")
print(my_dict)
my_dict.clear()
print(my_dict)

print("copy() --Return a shallow copy of the dictionary.")
my_copy_dict = my_dict.copy()
print(my_dict)
print(my_copy_dict)

print("fromkeys(iterable[, value]) --Create a new dictionary with keys from iterable and values set to value.")
my_new_dict = dict.fromkeys(["city","state","country","continent","planet","galaxy"],"Unknown")
print(my_new_dict)

print("""
      The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
      They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
      
      items()
        Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

      keys()
        Return a new view of the dictionary’s keys. See the documentation of view objects.
      
      values()
        Return a new view of the dictionary’s values.
      """)
print(my_new_dict.items())
print(my_new_dict.keys())
print(my_new_dict.values())

print("""
      pop(key[, default])
        If key is in the dictionary, remove it and return its value, else return default. 
        If default is not given and key is not in the dictionary, a KeyError is raised.
      """)

my_dict = {"name": "gaurav", "rollno": 1 , "city": "Pune","Subjects" : ["DBDA","DIOT","DAC","HPCSA"]}
print(my_dict)
print(my_dict.pop("name"))
#print(my_dict.pop("name1")) # KeyError: 'name1'
print(my_dict.pop("name1","defaulted"))

print("""
      popitem()
        Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
      """)
print(my_dict.popitem())

print("""
      reversed(d)
      Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).
      """)

print(my_dict)
print(list(reversed(my_dict)))
print(list(reversed(my_dict.keys())))
print(list(reversed(my_dict.values())))
print(dict(reversed(my_dict.items())))


  
print("""
      setdefault(key[, default])
        If key is in the dictionary, return its value. 
        If not, insert key with a value of default and return default. 
        default defaults to None.
      """) 
  
print(my_dict)   
print(my_dict.setdefault("name1","new_field_value"))
print(my_dict)   

print(""" 
      update([other])
        Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
      """)

print(my_dict)   
my_dict.update({"state":"MH","gender" : "male"})
print(my_dict)   
my_dict.update([('foo', 100), ('bar', 200)])
print(my_dict)   

print("""
      d | other
        Create a new dictionary with the merged keys and values of d and other, 
        which must both be dictionaries. 
        The values of other take priority when d and other share keys.
      """)
my_dict = {"name":"gaurav"}
my_new_dict = {"rollno" : 1}
print(my_dict)
print(my_new_dict)
print(my_dict|my_new_dict)
print(my_dict)


print(""" 
      d |= other
        Update the dictionary d with keys and values from other,
        which may be either a mapping or an iterable of key/value pairs. 
        The values of other take priority when d and other share keys.
      """)

print(my_dict)
print(my_new_dict)
my_dict|= my_new_dict
print(my_dict)

print("Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering).")

my_dict = {"name" : "gaurav","rollno":1}
my_new_dict = {"rollno":1,"name" : "gaurav"}
my_newer_dict = {"rollno":1,"name" : "gaurav","state":"MH"}

print(my_dict == my_new_dict)
print(my_new_dict == my_newer_dict)
               