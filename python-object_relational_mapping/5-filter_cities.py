#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Use parameterized query to retrieve cities of the specified state
        query = ("SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ') "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s")
        cursor.execute(query, (state_name,))

        # Fetch the result
        result = cursor.fetchone()[0]

        # Print the result
        if result:
            print(result)
        else:
            print("No cities found for the specified state.")

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
