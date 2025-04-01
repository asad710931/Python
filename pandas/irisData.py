import pandas as pd
import matplotlib.pyplot as plt

#iris_data=pd.read_csv("iris.csv")
iris_data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv")

print(iris_data.head())
# print(iris_data.tail())
# print(iris_data.describe())

iris_new_data=iris_data[["sepal_length","species"]]
# print(iris_new_data)
filtered_data=iris_data[(iris_data["sepal_length"]>5.0) & (iris_data["species"]=="setosa")]

print(filtered_data)