this_dict ={'name':'ali','age':25}
print(this_dict['name'])
this_dict['city']='lahore'
print(this_dict)
this_dict['age']=30
print(this_dict)
del this_dict['age']
print(this_dict)
if 'salary' in this_dict:
    print(this_dict['salary'])
else:
    print('salary key is not present in the dictionary')
print(this_dict.keys())
print(this_dict.values())
print(this_dict.items())
print(this_dict.get('score', 'default value'))
keys=['a','b']
value=[1,2]
my_dict=dict(zip(keys,value))
print(my_dict)