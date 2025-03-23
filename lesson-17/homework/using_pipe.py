import pandas as pd
import os

os.chdir(r"C:\Python\pythonhomeworks\lesson-17")

# 1.Pipeline on Titanic
try:
    df_titanic = pd.read_excel("data/titanic.xlsx")
    def filter_passengers(df):
        return df[df["Survived"]==1].copy()
    def fill_ages(df):
        df.loc[:,"Age"] = df["Age"].fillna(df["Age"].mean())
        return df
    def new_column(df):
        df.loc[:,"Fare_Per_Age"] = df["Fare"] / df["Age"]
        return df
    df_titanic_pipe = (df_titanic.pipe(filter_passengers).pipe(fill_ages).pipe(new_column))
    print(df_titanic_pipe.sample(5))
except FileNotFoundError:
    print("File not found!")

# 2.Pipeline on Flights
try:
    df_flights = pd.read_parquet("../data/flights")
    def filter_departure_delay(df):
        return df[df["Delay"]>30]
    def delay_per_hour(df):
        df["Delay_Per_Hour"] = df["Delay"]/df["Duration"]
        return df
    df_flights_delay=df_flights.pipe(filter_departure_delay).pipe(delay_per_hour)
    print(df_flights_delay)
except FileNotFoundError:
    print("File not found!")