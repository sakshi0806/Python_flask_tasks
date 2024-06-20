
# DICTIONARY

#student = {'name': 'Sakshi', 'age': 21, 'courses': ['Maths', 'CompSci']}
#print(student)

#employe = {'name':'Idrees Bhat','qualification':'PhD','Address':'J&K'}
#print(employe)

#student1 = {'name': 'BHakti', 'age': 18, 'courses': ['Physics', 'Chemistry']}
#print(student)

#student2 = {'name': 'Om', 'age': 16, 'courses': ['History', 'Geometry']}
#print(student)

# acessing indvidual key from dictionary

#print(student['name'])
#print(student['age'])
#print(student['courses'])

student = {1: 'Sakshi', 'age': 21, 'courses': ['Maths', 'CompSci', 'AI']}
#print(student[1])
#print(student['Bhakti'])
#print (student.get('age'))
#print (student.get('Om'))

#print (student.get('age','Key does not exist!!!'))
#print (student.get('aiwa','Key does not exist!!!'))

#student['University'] = 'MIT WORLD PEACE UNIVERSITY'
#print (student)

# update method
#student.update({'one':1,'two':2,'three':3,'four':4,'five':5})
#print(student)

# deleting a key
#print(student1)
#del student1['age']
#print(student1)

#value_deleted = student1.pop('courses')
#print ('we have deleted ' + str (value_deleted) + ' key from dictionary ')

# length of dictionary
#print(student2)
#print (len(student2))
#print (student2.keys())
#print(student2.values())
#print (student2.items())

print(student)
for key in student.keys():
    print(key)
for key in student.values():
    print(key)
for key, value in student.items():
    print(key, value)