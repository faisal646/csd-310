""" 
    Title: pysports_update_and_delete.py
    Author: Salahauddin Faisal
    Date: 28 February 2021
    Description: In this program, we will view, insert, 
                update and delete rows in the player2 table.
"""

""" imports """
import mysql.connector
from mysql.connector import errorcode


""" Config object to connect to the database """
config = {
    "user": "faisal646",
    "password": "ABCD1234",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


# Creating a function to display player's information in player2 table.
def all_players(cursor_object):
    # Stablishing inner join
    cursor_object.execute("SELECT playerID, Firstname, Lastname, Team_name FROM player2 INNER JOIN team2 ON player2.Team_id = team2.Team_id")

    # get results from the cursor object 
    players = cursor_object.fetchall()

     # Displaying players Info. 
    for player in players:
       print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))



try:
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()


    # Calling function to display all player's information.....................
    print("\nShowing player's info in the player2 table.........\nBefore inserting any new data.............\n")
    all_players(cursor)



    # Syntax for inserting new player...........................................
    insert_new_player = ("INSERT INTO player2(Firstname, Lastname, Team_id) VALUES (%s, %s, %s)")

    # New player info 
    new_player_info = ("Tom", "Gold", 4)
    player_info_to_update = ("Jasim", "Uddin", 4)

    # Insertion of a new player in the mentioned Database table. (player2)
    cursor.execute(insert_new_player, new_player_info)
    cursor.execute(insert_new_player, player_info_to_update)

    # commiting new player to the database
    db.commit()

    # Printing updated player info from player2 table after database commit.
    print("\n\nPlayer2 table, with new player info..........\n")
    all_players(cursor)
    


    # Updating a player's data.......................................................
    update_player_data = ("UPDATE player2 SET Team_id = 4, Firstname = 'Jane', Lastname = 'Doe' WHERE Firstname = 'Jasim'")

    # execute the update query
    cursor.execute(update_player_data)
    db.commit()

    # Printing player2 table data after updating a player info
    print("\n\nUpdated player2 table, A player info is changed......\n")
    all_players(cursor)



    # Deleting a player from player2 table............................................
    #cursor.execute("DELETE FROM player2 WHERE Firstname='Tom'")
    #cursor.execute("DELETE FROM player2 WHERE Firstname='John'")
    cursor.execute("DELETE FROM player2 WHERE Firstname='Jane'")
    db.commit()

    # Showing player's info after deleting a player.
    print("\n\nPrinting Player's data after removing a player from the player2 Database.....\n")
    all_players(cursor)

    print("\n\n----- END OF PROGRAM ----\n")




except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    # Closing connection
    db.close()