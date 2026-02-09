import pandas as pd
import numpy as np
data = [1,2,3,4]
ser = pd.Series(data)
print(ser)
data1 = np.array(['j','a','y','a','n','a','n','d','h','i','n','i','i'])
ser1 = pd.Series(data1)
print(ser1[:5])
ser2 = pd.Series(data1,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
print(ser2[16])

