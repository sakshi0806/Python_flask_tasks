# BUILT-IN MODULES 

#math
import math
print(math.sqrt(25)) 

#random
import random
print(random.randint(1, 100)) 

#datetime
import datetime
current_time = datetime.datetime.now()
print(current_time) 

# THIRD-PARTY PACKAGES (From PyPI)

#requests: Used for making HTTP requests
import requests
response = requests.get('https://www.google.com')
print(response.status_code) 

#numpy: Provides support for numerical computations and multidimensional arrays.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean()) 

#pandas: Pandas is built on top of numpy. Offers data manipulation and analysis tools.
import pandas as pd
data = {'Name': ['Sakshi', 'Bhakti', 'Om'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df) 

#matplotlib: Used for creating visualizations and plots.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 12]
plt.plot(x, y)
plt.show() 








