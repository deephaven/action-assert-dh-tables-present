"""
validate.py

A Python script that validates the presence of tables in Deephaven.

@author Jake Mulford
@copyright Deephaven Data Labs
"""
from pydeephaven import Session, DHError

import time

def main(table_names, host=None):
    """
    Main method for the script. Simply validates that each table exists

    Parameters:
        table_names (list<str>): A list of table names to validate
        host (str): An optional host if not using the default

    Returns:
        None
    """
    print("Attempting to connect to host at")
    print(host)
    print("Attempting to validate table names")
    print(table_names)
    session = None

    #Simple retry loop in case the server tries to launch before Deephaven is ready
    count = 0
    max_count = 5
    while (count < max_count):
        try:
            if host is None:
                session = Session()
            else:
                session = Session(host=host)
            count = max_count
        except:
            print("Failed to connect to Deephaven... Waiting to try again")
            time.sleep(5)
            count += 1
    if session is None:
        sys.exit("Failed to connect to Deephaven after 5 attempts")

    table = session.empty_table(3)
    for table_name in table_names:
        try:
            #session.open_table(table_name)
            #Temporary workaround: This script is sufficient to check that the table exists
            session.run_script("{table}={table}".format(table=table_name))
            print("Validates presence of table {table}".format(table=table_name))
        except DHError as e:
            print("Deephaven error when trying to open table {table_name}".format(table_name=table_name))
            print(e)
            exit(1)
        except Exception as e:
            print("Unexpected error when trying to open table {table_name}".format(table_name=table_name))
            print(e)
            exit(1)

usage = """
usage: python validate.py <table-names> host
"""

if __name__ == '__main__':
    import sys
    try:
        #For some reason, the workflow is passing sys.argv[1] with an extra set of
        #double quotes, so it's like '"value,value"'. This splice removes those quotes
        #before splitting on the comma
        table_names = sys.argv[1][1:-1].split(",")
    except:
        print(usage)
        exit(1)

    host = None
    if len(sys.argv) > 2:
        host = sys.argv[2][1:-1]

    main(table_names, host)
