import pandas as pd
import os

os.chdir(r"C:\Python\pythonhomeworks\lesson-17")

# 1.Apply a Custom Function on Titanic
try:
    df_titanic = pd.read_excel("data/titanic.xlsx")
    def child_or_adult(age):
        if not (age>0): return
        elif age<18: return "Child"
        else: return "Adult"
    df_titanic["Age_Group"] = df_titanic["Age"].transform(child_or_adult)
    print(df_titanic.sample(4))
except FileNotFoundError:
    print("File not found!")

# 2.Normalize Employee Salaries
try:
    df_employee = pd.read_csv("data/employee.csv")
    def min_max_normalize(series):
        return (series-series.min())/(series.max()-series.min())
    df_employee["NORMALIZED_SALARY"] = df_employee.groupby("DEPARTMENT")["BASE_SALARY"].transform(min_max_normalize)
    print(df_employee.head(5))
except FileNotFoundError:
    print("File not found!")

# 3.Custom Function on Movies
try:
    df_movie_data=pd.read_csv("data/movie.csv")
    def movie_duration(duration):
        if not duration>=0: return
        elif duration<60: return "Short"
        elif duration<120: return "Medium"
        else: return "Long"
    df_movie_data["duration_type"] = df_movie_data["duration"].apply(movie_duration)
    df_movie_duration=df_movie_data[["duration", "duration_type"]].sample(5)
    print(df_movie_duration)
except FileNotFoundError:
    print("File not found!")