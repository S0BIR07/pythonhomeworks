import sqlite3
with sqlite3.connect("roster.db") as connection:
    cursor=connection.cursor()
    query1="Create table if not exists Roster(Name text, Species text, Age int)"
    cursor.execute(query1)

    query2="Insert into Roster Values(?,?,?)"
    table=[
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)]
    cursor.executemany(query2,table)

    query3 = "Update Roster Set Name='Ezri Dax' Where Name='Jadzia Dax'"
    cursor.execute(query3)

    query4 = "Select Name, Age From Roster Where Species='Bajoran'"
    result4 = cursor.execute(query4)
    print(result4.fetchall())

    query5 = "Delete From Roster Where Age>100"
    cursor.execute(query5)

    cursor.execute("Alter Table Roster Add Column Rank text")
    data6 = [
        ("Benjamin Sisko", "Captain"),
        ("Ezri Dax", "Lieutenant"),
        ("Kira Nerys", "Major")
    ]
    for data in data6:
        query6 = f"Update Roster Set Rank='{data[1]}' Where Name='{data[0]}'"
        cursor.execute(query6)

    query7 = "Select * From Roster Order By Age Desc"
    result7 = cursor.execute(query7)
    print(result7.fetchall())