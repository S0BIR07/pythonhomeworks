import pandas as pd

try:
    # 1.iris.json
    df_iris = pd.read_json("data/iris.json")
    df_iris.columns = [column.lower() for column in df_iris.columns]
    print(df_iris[["sepalwidth", "sepallength"]])
except FileNotFoundError:
    print("File not found!")
try:
    # 2.titanic.xlsx
    df_excel = pd.read_excel("data/titanic.xlsx")
    print(df_excel[df_excel["Age"]>30])
    print(df_excel.value_counts("Sex"))
except FileNotFoundError:
    print("File not found!")
try:
    # 3.flight parquet file
    df_parquet = pd.read_parquet("data/flights")
    print(df_parquet[["origin", "dest", "carrier"]])
    print(len(set(df_parquet["dest"])))
except FileNotFoundError:
    print("File not found!")
try:
    # 4.movie.csv
    df_movie = pd.read_csv("data/movie.csv")
    df_filtered_movie = df_movie[df_movie["duration"]>120]
    df_filtered_movie.sort_values("director_facebook_likes", ascending=False, inplace=True)
    print(df_filtered_movie)
except FileNotFoundError:
    print("File not found!")