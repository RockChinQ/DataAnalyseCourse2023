import pandas as pd

# 读取数据
iris = pd.read_csv("iris.csv")

# 筛选出花萼长度大于6cm的数据
filtered_data = iris[iris["Sepal.Length"] > 6]

# 对品种进行分组，然后计算每个分组的大小（数据个数）
result = filtered_data.groupby("Species").size()
print(result)
