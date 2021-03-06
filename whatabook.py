""" 
    Title: whatabook.py
    Author: Salahauddin Faisal
    Date: March 04, 2021
    Description: WhatABook program that interacts with MySQL database using given credentials
"""

""" imports """
import sys
import mysql.connector
from mysql.connector import errorcode

""" Database Configuration """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Line 23, 24 is for testing the following program by myself. Please disregard.
#db = mysql.connector.connect(**config)  
#cursor = db.cursor() 

# Program to give the user a prompt to navigate through the different menu
def show_menu():
    print("\n  -- MAIN MENU --")
    print("\n  1. Books\n  2. Store Locations\n  3. Account\n  4. Exit")

    try:
        user_selection = int(input("\nPlease select an option from above menu to explore: "))
        return user_selection
    except ValueError:
        print("\nInvalid input, Program Terminated ---\n")
        sys.exit(0)

#show_menu()

# This program displays all the books in the database
def show_books(cursor_obj):
    # Retriving book's info from database 
    cursor_obj.execute("SELECT bookID, bookName, authorName, descriptions FROM book")
    # Storing all the books from the database into a python list 
    books = cursor_obj.fetchall()

    print("\nShowing all the Books")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("\nBook ID: {}\nBook Name: {}\nAuthor: {}\nDescription: {}\n".format(book[0], book[1], book[2], 
        book[3]))

#show_books(cursor)

# This program displays Book Store location.
def show_locations(cursor_obj):
    # Retriving store location from the store table in the database
    cursor_obj.execute("SELECT storeID, location FROM store")
    # Storing store location
    locations = cursor_obj.fetchall()

    print("\n--- STORE INFO ---: ")
    for location in locations:
        print("\nStore ID: {}\nLocation: {}\n".format(location[0], location[1]))

#show_locations(cursor)

# This program validates users by give ID number
def validate_user():
    try:
        userID = int(input('\nPlease enter an user id: '))
        if userID < 1 or userID > 3:
            print(userID, "is not a valid user id number, please try again ---\n")
            sys.exit(0)
        return userID

    except ValueError:
        print("\nIncorrect input, please try again ---")
        sys.exit(0)

#validate_user()

# This program displays the users account information.
def show_account_menu():
    try:
        print("\nUSER MENU\n")
        print("1. Wishlist\n2. Add a Book\n3. Main Menu")
        selected_option = int(input('Please select an option from above: '))
        if (selected_option < 1 or selected_option > 3):
            print("\nInvalid number.\nPlease select a valid option next time.")
            sys.exit(0)
        return selected_option

    except ValueError:
        print("\nInvalid input.\nEnd of Program.")
        sys.exit(0)
    
#show_account_menu()
# This program shows user info and book info from wishlist table
def display_wishlist(cursor_obj, userID):

    cursor_obj.execute("SELECT user.userID, user.firstName, user.lastName, book.bookID, book.bookName," +
                    "book.authorName " +
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.userID = user.userID " + 
                    "INNER JOIN book ON wishlist.bookID = book.bookID " + 
                    "WHERE user.userID = {}".format(userID))
    
    wishlist = cursor_obj.fetchall()

    print("\nShowing selected user's wish list.\n")
    for data in wishlist:
        print("Username: {} {}\nBook: {}\nAuthor: {}\n".format( data[1], data[2], data[4], data[5]))

#display_wishlist(cursor, 2)

# This program shows all the books that are not in a users wishlist
def show_books_to_add(cursor_obj, userID):
    """ query the database for a list of books not in the users wishlist """
    print("Showing which books can be added in the wishlist.")
    cursor_obj.execute("SELECT bookID, bookName, authorName, descriptions FROM book WHERE bookID NOT IN (SELECT bookID FROM wishlist WHERE userID = {})".format(userID))
    available_books = cursor_obj.fetchall()

    print("\n--- DISPLAYING AVAILABLE BOOKS ---\n")
    for book in available_books:
        print("Book Id: {}\nBook Name: {}\nAuthor: {}\nDescription: {}\n".format(book[0], book[1], book[2], book[3]))

#show_books_to_add(cursor, 3)

# This program adds books to users wish list
def add_book_to_wishlist(cursor_obj, bookID, userID):
    cursor_obj.execute("INSERT INTO wishlist(userID, bookID) VALUES({}, {})".format(userID, bookID))


#def add_book_to_wishlist(cursor_obj, bookID, userID, db):
#   cursor_obj.execute("INSERT INTO wishlist(userID, bookID) VALUES({}, {})".format(userID, bookID))
#   db.commit()
#add_book_to_wishlist(cursor, 5, 1, db)





try:
    """ try/catch block for handling potential MySQL database errors """ 
    # Stablising connection to whatabook database 
    db = mysql.connector.connect(**config) 
    # Cursor object for making executing sql queries
    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")
    # Shows the main menu and prompt users to select an option
    user_selection = show_menu() 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)
            
        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            userID = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    display_wishlist(cursor, userID)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:
                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, userID)

                    # get the entered book_id 
                    bookID = int(input("\nEnter the id of the book you want to add: "))

                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, userID, bookID)
                    # commit the changes to the database
                    db.commit()  

                    print("\nBook id: {} was added to your wishlist!".format(bookID))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 1 or user_selection > 4:
            print("\nInvalid option, please retry...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...\n\n")


except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()