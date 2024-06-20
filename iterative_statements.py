
# PYTHON LOOPS                               

my_list = [1,2,3,4,5,6,7,8,9,10]
# print(my_list)

# #to use loop

# for num in my_list:
#      print (num)
    
    
# usage of Break and continue statements

# BREAK

for num in my_list:
    
      if num == 6:
        
          break
    
      else:
        
          print ('SAKSHI is here')


# CONTINUE STATEMENT

for num in my_list:
    
     if num == 6:
       print ("SAKSHI is here") 
       continue
    
#        #print ("SAKSHI is here")
    
else:
        
       print ('MIT WPU Kothrud')


# LOOP WITH IN A LOOP

num = [1,2,3]

num_1 = [3,4,5]

for sakshi in num:
    
      for second in num_1:
        
         print ('TAG TEAM CHAMPIONSHIP',(sakshi,second))


# TO RUN A LOOP WITH CERTAIN NUMBER OF TIME


for i in range (10):
    
     print (i)


for i in range (10.20): 
          print (i)
    

# difference between definite and indefinite loops

first_number = 0
while first_number != 20:
    
         print (first_number)
         first_number += 1
         
         
         
         
# use of do while statement
         
counter = 1

while True:
    
    print("This is iteration", counter)
    
    counter += 1

    if counter >= 10:
        break         













