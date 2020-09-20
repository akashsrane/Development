emp_1 = {'name':'Aakash','age':21,'location':'Pune'}
print(emp_1['name'])
print(emp_1['age'])
print(emp_1['location'])
print(emp_1)
emp_1['qualification'] = 'graduate'
emp_1['height'] = '6-feet'
print(emp_1)

emp_2 = {}
emp_2['name'] = 'Onkar'
emp_2['age'] = 21
emp_2['location'] = 'Goa'
print(emp_2)
print(f"{emp_2['name']} was {emp_2['age']} years old")
emp_2['age'] = 22
print(f"{emp_2['name']} is now {emp_2['age']} years old")

print(len(emp_1))