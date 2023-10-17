import pandas as pd

# 读取数据
iris = pd.read_csv("iris.csv")

# 对品种进行分组，然后计算最小值和平均值
result = iris.groupby("Species").agg(["min", "mean"])
print(result)
