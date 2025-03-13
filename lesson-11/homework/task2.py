import sqlite3
with sqlite3.connect("Library.db") as connection:
    cursor=connection.cursor()
    query_1="Create table if not exists Books(Title text, Author text, Year_Published int, Genre text)"
    cursor.execute(query_1)
    data_2=[
        ('To Kill a Mockingbird',	'Harper Lee',	1960,	'Fiction'),
        ('1984',	'George Orwell',	1949,	'Dystopian'),
        ('The Great Gatsby',	'F. Scott Fitzgerald',	1925,	'Classic')
    ]
    query_2="Insert into Books Values(?,?,?,?)"
    cursor.executemany(query_2,data_2)
    query_3 = "Update Books Set Year_Published=1950 Where Title='1984'"
    cursor.execute(query_3)
    query_4 = "Select Title, Author From Books Where Genre='Dystopian'"
    result_4 = cursor.execute(query_4)
    print(result_4.fetchall())
    query_5 = "Delete From Books Where Year_Published<1950"
    cursor.execute(query_5)
    data_6 = [
        ("To Kill a Mockingbird", 4.8),
        ("1984", 4.7),
        ("The Great Gatsby", 4.5)
    ]
    query_6_1 = "Alter Table Books Add Column Rating float(1, 1)"
    cursor.execute(query_6_1)
    for data in data_6:
        query_6_2 = f"Update Books Set Rating={data[1]} Where Title='{data[0]}'"
        cursor.execute(query_6_2)
    query_7 = "Select * From Books Order By Year_Published Asc"
    result_7 = cursor.execute(query_7)
    print(result_7.fetchall())