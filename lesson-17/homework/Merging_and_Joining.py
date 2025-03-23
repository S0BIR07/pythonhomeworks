import sqlite3
import pandas as pd
import os

os.chdir(r"C:\Python\pythonhomeworks\lesson-17")

# 1.Inner Join on Chinook Database
try:
    with sqlite3.connect("data/chinook.db") as connection:
        df_customers = pd.read_sql(
            "SELECT * FROM customers",
            con=connection
        )
        df_invoices = pd.read_sql(
            "SELECT * FROM invoices",
            con=connection
        )
    inner_join = pd.merge(df_customers, df_invoices, on="CustomerId")
    total_invoices = inner_join.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="TotalInvoices")
    print(total_invoices.head())
except sqlite3.OperationalError:
    print("Unable to open database file")

# 2.Outer Join on Movie Data
try:
    df_movie_data=pd.read_csv("data/movie.csv")
    df_director_name_color=df_movie_data[["director_name", "color"]]
    df_director_name_num_critic_for_reviews=df_movie_data[["director_name","num_critic_for_reviews"]]
    left_join = pd.merge(df_director_name_color, df_director_name_num_critic_for_reviews, on="director_name", how="left")
    outer_join = pd.merge(df_director_name_color, df_director_name_num_critic_for_reviews, on="director_name", how="outer")
    print("Left join rows: ", left_join.shape[0])
    print("Outer join rows: ", outer_join.shape[0])
except FileNotFoundError:
    print("File not found!")