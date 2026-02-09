import matplotlib.pyplot as plt
import numpy as np
fruits = ['Apples','Bananas','Cherries','Dates']
sales = [400,350,300,450]
plt.barh(fruits,sales,color='violet')
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Fruit Sales")
plt.show()

