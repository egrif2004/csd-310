
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def main_menu():
    print("\n  ...Main Menu...")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        selection = int(input(' press 1,2,3,or 4, for selections'))

        return selection
    except ValueError:
        print("\n  wrong number try again.\n")

        sys.exit(0)

def display_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  ...Book Selections...")
    
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  ...STORE LOCATIONS...")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def authenticate_user():
    ###have user select their id###

    try:
        user_id = int(input('\n pick user_id between 1 to 3 '))

        if user_id < 0 or user_id > 3:
            print("\n  wrong customer number, goodbye!\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n wrong number, goodbye! \n")

        sys.exit(0)

def show_users_menu():
    ###Shows user menu###

    try:
        print("\n      ...User's Menu...")
        print("     press 1 for Wishlist\n        press 2 for Add Book\n       press 3 for Main Menu")
        account_option = int(input(' press the corresponding number'))

        return account_option
    except ValueError:
        print("\n  wrong number, goodbye!\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n       ... Wishlist Books...")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_book_selection(_cursor, _user_id):
    ### book selection

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n    ...Book Selection list...")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) ####connect to the WhatABook database using the config

    cursor = db.cursor() 

    print("\n  .....Welcome to the WhatABook store..... ")

    user_selection = main_menu() # show the main menu 

    # while loop to keep menu open because 4 closes program 
    while user_selection != 4:

        # #1 displays books
        if user_selection == 1:
            display_books(cursor)

        # #2 shows store locations
        if user_selection == 2:
            show_locations(cursor)

        # #3  prompts user to verify userid
        if user_selection == 3:
            my_user_id = authenticate_user()
            account_option = show_users_menu()

            ###while loop while input is not 3 because 3 sends user back to main menu###
            while account_option != 3:

                ### if the use selects option 1, show wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # 
                if account_option == 2:

                    show_book_selection(cursor, my_user_id)

                    book_id = int(input("\n        Enter the id number of the book you want to add to your wishlist: "))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))
 
                if account_option < 0 or account_option > 3:
                    print("\n      wrong number error, please try again.")
                account_option = show_users_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("\n      wrong number error, please try again...")
            
        user_selection = main_menu()

    print("\n\n Come back soon goodbye!")

except mysql.connector.Error as err:
    ###sql user account errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Theusername or password are incorrect")
 
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  Incorrect database")

    else:
        print(err)

finally:
  ### close database###  
 db.close()