
# DATA STRUCTURES IN PYTHON
#lists

#list_1 = ['English','Maths','Science','History','Marathi']
#print(list_1)

#print(len(list_1))

#print(list_1[2])
#print(list_1[4])
#print(list_1[-1])
#print(list_1[-4])
#print(list_1[-5])
#print(list_1[-6])
#print(list_1[5])

#list_2 = ['Red','Yellow','Blue','Green','Purple']
#print(list_2)
#a = len(list_2)-1
#print(list_2[a])

# range of values
#print(list_2[0:2])
#print(list_2[:2])
#print(list_2[0:4])
#print(list_2[0:])
#print(list_2[:])

#list_2.append('Brown')
#print(list_2)
#list_2.insert(1, 'Black')
#print(list_2)

#list_3 = ['White','Olive Green','Light Blue']
#list_2.extend(list_3)
#print(list_2)

#list_2.insert(1,list_3)
#print(list_2)

#list_2.remove('White')
#print(list_2)

#list_2.remove('Yellow')
#print(list_2)

#print(list_2.pop(6))

my_list = ['Pune','Mumbai','Satara','Nashik','Jalgaon']

# reverse a list
#print(my_list)
#my_list.reverse()
#print(my_list)

# sort 
#my_list.sort()
#print(my_list)

#num_list = [34,25,-3,76,45,0,98,10]

#print(num_list)
#num_list.sort() #ascending order
#print(num_list)
#num_list.sort(reverse=True) #descending order
#print(num_list)

#sorted(num_list)
#print(num_list)
#new_list = sorted(num_list)
#print(num_list)
#print(new_list)

#print(min(num_list))
#print(max(num_list))

print(my_list)
#print(my_list.index('Satara'))
#print(my_list.index('aaaaa'))

#print('ggg' in my_list)
#print('Pune' in my_list)

# iteration
for item in my_list:
    print(item)
    
# enumerate function
for index, item in enumerate(my_list):
    print(index, item)
    
for index, item in enumerate(my_list, start=100):
    print(index, item)
    
# transforming lists into strings
print(my_list)
list_to_string = '-'.join(my_list)
print(list_to_string)

new_list = list_to_string.split('-')
print(new_list)
    
