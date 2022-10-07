import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans


df = pd.read_csv("diabetes.csv")
print(df)
df2 = df['Outcome'].value_counts()
print(df2)
# sns.scatterplot(x='', y='BloodPressure', data=df2, s=60, color='green')
# plt.savefig('scatterplot.png', dpi=100)
# N, P = df['Outcome'].value_counts()

