from lyrics import *
import  sqlite3
conn  =  sqlite3 . connect ( 'Lyrics_database.db' )
cursor  =  conn.cursor ()
#create the salesman table 
cursor.execute("CREATE TABLE IF NOT EXISTS songlyrics (id n(5), artist_name char(30), track_name char(35), lyrics char(300));")




def insert_data(data):
    conn  =  sqlite3 . connect ( 'Lyrics_database.db' )
    cursor  =  conn.cursor ()

    cursor.execute("""
    INSERT INTO songlyrics(id, artist_name, track_name, data)
    VALUES (?,?,?,?)
    """,(id, artist_name, track_name, data))
    conn.commit ()
    print ( 'Data entered successfully.' )
    conn . close ()
    if (conn):
        conn.close()
        print("\nThe SQLite connection is closed.")


def select_data():
    conn  =  sqlite3 . connect ( 'Lyrics_database.db' )
    cursor  =  conn.cursor ()

    # function that prints out the data saved in the database
    cursor = conn.execute("SELECT  artist_name, track_name, lyrics from songlyrics")
    for row in cursor:
        print ("artist_name = ")
        print ("track_name = ")
        print("Lyrics = ""\n")
    print("Operation done successfully")
    # closes after printing the data
    conn.close()