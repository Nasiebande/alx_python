#!/usr/bin/python3
"""Script to list all State objects containing the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Fetch State objects containing the letter 'a' and print their details
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
    .order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
