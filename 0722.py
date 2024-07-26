import pandas as pd

mpg = pd.read_csv("data/mpg.csv")
mpg.shape()

!pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=mpg,
                x = 'displ', y = 'hwy', 
                hue="drv").set(xlim=[3,6], ylim=[10, 30])
plt.show()
plt.clf()

# 막대 그래프 # drv 새로운 칼럼이 됨
df_mpg = mpg.groupby("drv", as_index=False) \ 
    .agg(mean_hwy=('hwy', 'mean'))
    
mpg["drv"].unique()

sns.barplot(data=df_mpg, 
            x = "drv", y = "mean_hwy",
            hue = "drv")

plt.show()
plt.clf()

sns.barplot(data=df_mpg.sort_values("mean_hwy", ascending = False), 
            x = "drv", y = "mean_hwy",
            hue = "drv")

plt.show()
plt.clf()

# 208p
df_mpg = mpg.groupby("drv", as_index = False) \
            .agg(n = ("drv", "count"))

sns.barplot(data = df_mpg, x = "drv", y ="n")
sns.countplot(data = mpg, x = "drv")

plt.show()
plt.clf()

df_mpg.view()













