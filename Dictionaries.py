#Dictionary is an ordered collection of data item. They store multiple items in single variable. 
#They are key value pairs and are enclosed by curly brackets

Dict={"name":"Sehar", "Field":"Cs", "Age":"19"}
print(Dict)

#Accessing single variable 
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}#syntax for dictionary definition
print(Dict)
print(Dict.keys())
print(Dict.values())

for key in Dict.keys():
  print(f"The value corresponding to the key {key} is {Dict[key]}")


#dictionary methods
#.get ---> ye specific key ki value display krta h
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
print(Dict.get('name'))#output: sehar

#.keys-->ye keys ka name/label dipaly krta ha
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
print(Dict.keys())#output: dict_keys(['name', 'Field', 'Age'])

#.values-->ye keys ki valu deta ha
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
print(Dict.values()) #output: dict_values(['sehar', 'Cs', '19'])

#.items-->sari key-value pairs me display krta ha
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
print(Dict.items()) #dict_items([('name', 'sehar'), ('Field', 'Cs'), ('Age', '19')])

#.update--> to update key-pairs
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
print(Dict.update({'Car':'BMW', 'city':'NewYork'}))
print(Dict)#output:{'name': 'sehar', 'Field': 'Cs', 'Age': '19', 'Car': 'BMW', 'city': 'NewYork'}

#popitem-->Removes and returns the last inserted key-value pair as a tuple.
Dict={'name':'sehar', 'Field':'Cs', 'Age':'19'}
item=Dict.popitem()
print(item) #update method me 2 items ko add kiya tah last pe ye un 2 last items ko remove kr deta h
print(Dict) #{'name': 'sehar', 'Field': 'Cs'}

#.clear--->Removes all items from the dictionary, leaving it empty.
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)                    # Output: {}

#.copy---> ye dictionary ki shallow copy create krta ha
my_dict = {'name': 'Alice', 'age': 25}
my_dict.copy()
print(my_dict) #output: {'name': 'Alice', 'age': 25}

#setdefault--->Is me agr koi specufic value nhi di jati to ye us ko deafult value de deta ha
my_dict={'name':'Sehar', 'age': 22}
value=my_dict.setdefault('city','unknown')
print(value)   #output: unknown
print(my_dict) #output: {'name': 'Sehar', 'age': 22, 'city': 'unknown'}

