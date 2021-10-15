import sqlite3

try:
    
    sqliteConnection = sqlite3.connect('Movies.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    sqlite_insert_query = """CREATE TABLE IF NOT EXISTS Movies(MovieName TEXT NOT NULL,Name_of_lead_actor TEXT NOT NULL,actress TEXT NOT NULL,year_of_relaese INTEGER,director_name TEXT NOT NULL) """

    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """INSERT INTO Movies VALUES ('Sherlock_Homes ','Robert_Downey ','Rachel_McAdams ',2011 ,'Guy_Ritchie ')"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """INSERT INTO Movies VALUES ('Baahubali ','Prabas ','Tamannaah',2015 ,'S S Rajamouli')"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """INSERT INTO Movies VALUES ('Ra.One ','Shah_Rukh_Khan ','Kareena Kapoor',2011 ,'Anubhav sinha')"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """INSERT INTO Movies VALUES ('Hera Pheri','Akshay Kumar','Tabu ',2000 ,'Priyadarshan')"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """SELECT * FROM Movies"""
    count = cursor.execute(sqlite_insert_query)
    result = cursor.fetchall();
    print(result);

    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
