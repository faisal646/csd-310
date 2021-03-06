import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "faisal646",
    "password": "ABCD1234",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    # Stablishing inner join
    cursor.execute("SELECT playerID, Firstname, Lastname FROM player2 INNER JOIN team2 ON player2.Team_id = team2.Team_id")

    # get results from the cursor object 
    players = cursor.fetchall()

     # Displaying players Info. 
    print()
    for player in players:
       print("Player ID: {}\nFirst Name: {}\nLast Name: {}\n".format(player[0], player[1], player[2]))


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