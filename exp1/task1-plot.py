import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
iris = pd.read_csv("iris.csv")

sns.scatterplot(data=iris, x="Sepal.Length", y="Sepal.Width", hue="Species")
plt.show()

sns.boxplot(data=iris, x="Species", y="Petal.Length")
plt.show()

sns.violinplot(data=iris, x="Species", y="Petal.Length")
plt.show()
