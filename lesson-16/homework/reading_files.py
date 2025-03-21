import sqlite3
import pandas as pd

# 1.chinook.db
try:
    with sqlite3.connect('data/chinook.db') as connection:
        df_customers = pd.read_sql(
            "SELECT * FROM customers",
            con=connection
            )
    print(df_customers.head(10))
except sqlite3.OperationalError:
    print("Unable to open database file")
except FileNotFoundError:
    print("File not found!")

# 2.iris.json
try:
    df_iris = pd.read_json('data/iris.json')
    print(df_iris.shape)
    print(df_iris.columns)
except FileNotFoundError:
    print("File not found!")

# 3.titanic.xlsx
try:
    df_titanic = pd.read_excel('data/titanic.xlsx')
    print(df_titanic.head())
except FileNotFoundError:
    print("File not found!")

# 4.flights parquet file
try:
    df_parquet = pd.read_parquet("data/flights")
    print(df_parquet.info)
except FileNotFoundError:
    print("File not found!")

# 5.movie.csv
try:
    df_movie = pd.read_csv("data/movie.csv")
    print(df_movie.sample(10))
except FileNotFoundError:
    print("File not found!")