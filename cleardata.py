import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

data = pd.read_csv("./data.csv")
print(data.shape)
#print(data)
#data['Preferred Foot'].value_counts().head(50).plot.bar(color = 'purple')
#print(data['Age'].value_counts())
data['Age'].value_counts(sort = True).plot.bar(color="blue")
plt.show()

