import pandas as pd

try:
    # 1.iris.json 
    df_iris = pd.read_json("data/iris.json") #Connect .json file/convert to dataframe
    print("Mean: \n",df_iris.select_dtypes("number").mean()) #find mean for numbers in dataframe
    print("Median: \n",df_iris.select_dtypes("number").median()) #find median for numbers in dataframe
    print("Standart deviation:\n",df_iris.select_dtypes("number").std()) #find standart deviation for numbers in dataframe
except FileNotFoundError:
    print("File not found!")
try:
    # 2.titanic.xlsx
    df_excel = pd.read_excel("data/titanic.xlsx") #connect excel file/convert to dataframe
    min_age =df_excel["Age"].min() #minimum age of passengers in dataframe
    max_age = df_excel["Age"].max() #maximum age of passengers in dataframe
    sum_age = df_excel["Age"].sum() #sum of ages of passengers in dataframe
    print(f"Min: {min_age}, max: {max_age}, sum: {sum_age}")
except FileNotFoundError:
    print("File not found!")
try:
    # 3.movie.csv
    df_movie = pd.read_csv("data/movie.csv") #connect csv file/convert to dataframe
    df_director_likes = df_movie.groupby("director_name")[["director_facebook_likes"]].sum() #sum of director facebook likes by director names in df
    print(f"Director: {df_director_likes.idxmax()}, Total likes: {df_director_likes.max()}")
    df_director_likes.sort_values("director_facebook_likes", ascending=False, inplace=True)
    print(f"Top 5:\n {df_director_likes.head(5)}")
except FileNotFoundError:
    print("File not found!")
try:
    # 4.flights parquet file
    df_parquet = pd.read_parquet("data/flights") #connect parquet file/convert to dataframe
    num_cols = df_parquet.select_dtypes("number").columns #select column with numbers
    df_parquet[num_cols] = df_parquet[num_cols].apply(lambda col: col.fillna(col.mean())) #fill missing values with mean of numbers in this column
except FileNotFoundError:
    print("File not found!")