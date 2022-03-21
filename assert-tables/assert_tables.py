"""
assert_tables.py

A Python script that asserts the presence of tables in Deephaven.

@copyright Deephaven Data Labs
"""
from pydeephaven import Session, DHError

import sys
import time

def main(table_names: str, host: str, port: int, session_type: str, max_retries: int):
    """
    Main method for the script. Simply asserts that each table exists

    Parameters:
        table_names (list<str>): A list of table names to assert the presence of
        host (str): The host name of the Deephaven instance
        port (int): The port on the host to access
        session_type (str): The Deephaven session type
        max_retries (int): The maximum attempts to retry connecting to Deephaven

    Returns:
        None
    """
    print(f"Attempting to connect to host at {host} on port {port}")

    session = None

    #Simple retry loop in case the server tries to launch before Deephaven is ready
    count = 0
    while (count < max_retries):
        try:
            session = Session(host=host, port=port)#, session_type=session_type)
            print("Connected to Deephaven")
            break
        except DHError as e:
            print("Failed to connect to Deephaven... Waiting to try again")
            print(e)
            time.sleep(5)
            count += 1
        except Exception as e:
            print("Unknown error when connecting to Deephaven... Waiting to try again")
            print(e)
            time.sleep(5)
            count += 1
    if session is None:
        sys.exit(f"Failed to connect to Deephaven after {max_retries} attempts")

    print("Attempting to assert presence of table names")
    print(table_names)

    for table_name in table_names:
        try:
            #session.open_table(table_name)
            #Temporary workaround: This script is sufficient to check that the table exists
            session.run_script(f"{table_name}={table_name}")
            print(f"Table is present: {table_name}")
        except DHError as e:
            print(e)
            sys.exit(f"Deephaven error when trying to access table: {table_name}")
        except Exception as e:
            print(e)
            sys.exit(f"Unexpected error when trying to access table: {table_name}")

usage = """
usage: python assert_tables.py table-names host port session-type max-retries
"""

if __name__ == '__main__':
    if len(sys.argv) > 6:
        sys.exit(usage)

    try:
        table_names = sys.argv[1].split(",")
        host = sys.argv[2]
        port = int(sys.argv[3])
        session_type = sys.argv[4]
        max_retries = int(sys.argv[5])
    except:
        sys.exit(usage)

    main(table_names, host, port, session_type, max_retries)
