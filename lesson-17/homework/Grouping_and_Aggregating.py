import pandas as pd
import os

os.chdir(r"C:\Python\pythonhomeworks\lesson-17")

# 1.Grouped Aggregations on Titanic
try:
    df_titanic = pd.read_excel("data/titanic.xlsx")
    df_titanic_info = df_titanic.groupby("Pclass").agg({
        "Age":"mean",
        "Fare":"sum",
        "PassengerId":"count"
    }).reset_index()
    df_titanic_info.columns = ["Pclass", "Average Age", "Total Fare", "Total Passengers"]
    print(df_titanic_info)
except FileNotFoundError:
    print("File not found!")

# 2.Multi-level Grouping on Movie Data
try:
    df_movie_data=pd.read_csv("data/movie.csv")
    df_multi_level_grouping = df_movie_data.groupby(["color", "director_name"]).agg(
        {
            "num_critic_for_reviews":"sum",
            "duration":"mean"
        }
    ).reset_index()
    print(df_multi_level_grouping)
except FileNotFoundError:
    print("File not found!")

# 3.Nested Grouping on Flights
try:
    df_flights = pd.read_parquet("../data/flights")
    df_nested_group_flights =df_flights.groupby(["Year", "Month"]).agg(
        {
            "FlightId":"count",
            "ArrDelay":"mean",
            "DepDelay":"max"

        }
    )
    print(df_nested_group_flights)
except FileNotFoundError:
    print("File not found!")