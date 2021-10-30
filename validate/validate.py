"""
validate.py

A Python script that validates the presence of tables in Deephaven.

@copyright Deephaven Data Labs
"""
from pydeephaven import Session, DHError

import time

def main(table_names: str, host: str, max_retries: int):
    """
    Main method for the script. Simply validates that each table exists

    Parameters:
        table_names (list<str>): A list of table names to validate
        host (str): The host name of the Deephaven instance
        max_retries (int): The maximum attempts to retry connecting to Deephaven

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
    while (count < max_retries):
        try:
            session = Session(host=host)
            continue
        except DHError as e:
            print("Failed to connect to Deephaven... Waiting to try again")
            print(e)
            time.sleep(5)
            count += 1
        except Exception as e:
            print("Unknown error when connecting to Deephaven")
            print(e)
            sys.exit()
    if session is None:
        sys.exit("Failed to connect to Deephaven after %d attempts" % max_retries)

    table = session.empty_table(3)
    for table_name in table_names:
        try:
            #session.open_table(table_name)
            #Temporary workaround: This script is sufficient to check that the table exists
            session.run_script("%s=%s" % (table_name, table_name))
            print("Table is present: %s" % table_name)
        except DHError as e:
            print("Deephaven error when trying to access table: %s" % table_name)
            print(e)
            exit(1)
        except Exception as e:
            print("Unexpected error when trying to access table: %s" % table_name)
            print(e)
            exit(1)

usage = """
usage: python validate.py table-names host max-retries
"""

if __name__ == '__main__':
    import sys

    print(sys.argv)

    if len(sys.argv) > 4:
        print(usage)
        exit(1)

    try:
        #For some reason, the workflow is passing sys.argvs with an extra set of
        #double quotes, so it's like '"value,value"', which is why we use string replace
        #before splitting on the comma
        table_names = sys.argv[1].replace('"', '').split(",")
        host = sys.argv[2].replace('"', '')
        max_retires = int(sys.argv[3].replace('"', ''))
    except:
        print(usage)
        exit(1)

    main(table_names, host, max_retries)
