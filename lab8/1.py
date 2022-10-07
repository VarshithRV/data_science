# person diabetic if glucose level > 160

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv("diabetes.csv")
# print(df)
print(df.columns)

sns.scatterplot(x='Glucose', y='BloodPressure', data=df, s=60, color='green')
plt.savefig('scatterplot.png', dpi=100)

x = df[['Glucose', 'BloodPressure']].values
model = KMeans(n_clusters=2, random_state=0).fit(x)

print(model.labels_)
print(model.cluster_centers_)

