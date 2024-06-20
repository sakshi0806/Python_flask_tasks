# READING A FILE
f = open('myfile.txt','r')
print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE
f = open('myfile2.txt','w')
f.write('Hello,Sakshi!')
f.close()

# APPEND A FILE
f = open('myfile2.txt','a')
f.write('Hello,Sakshi! HOW ARE YOU ')
f.close()

with open('myfile2.txt','a')as f:
  f.write("Hello")

# readlines() method
f = open('myfile3.txt','r')
while True:
    line = f.readline()
    print(line, type(line))
    if not line:
      break

# writelines() method
f = open('mytxt.txt','w')
lines = ['line 1\n', 'line 2\n', 'line 3\n','line 4\n']
f.writelines(lines)
f.close()

# seek() function
with open('myfile.txt','r') as f:
  print(type(f))
  f.seek(10) #move to the 10th byte in the file
  data = f.read(8) # read next 8 bytes
  print(data)

# tell() function
with open('myfile.txt','r') as f:
  print(type(f))
  f.seek(10) #move to the 10th byte in the file
  print(f.tell())
  data = f.read(8) # read next 8 bytes
  print(data)


# error handling with files

# opening and reading files
try:
  with open('filename.txt', 'r') as file:
      content = file.read()

except FileNotFoundError:
  print("File not found or cannot be opened.")
except IOError:
  print("Error reading the file.")
except Exception as e:
  print("An error occurred:", str(e))

# opening and writing files
try:
  with open('output.txt', 'w') as file:
      file.write("Error handling with files")
except IOError:
  print("Error writing to the file.")
except Exception as e:
  print("An error occurred:", str(e))

