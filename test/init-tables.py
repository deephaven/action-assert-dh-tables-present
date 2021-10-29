"""
init-tables.py

A Python script that adds a few tables to Deephaven.

@author Jake Mulford
@copyright Deephaven Data Labs
"""
from pydeephaven import Session

import time

session = None

#Simple retry loop in case the server tries to launch before Deephaven is ready
count = 0
max_count = 5
while (count < max_count):
    try:
        session = Session()
        count = max_count
    except:
        print("Failed to connect to Deephaven... Waiting to try again")
        time.sleep(2)
        count += 1

if session is None:
    sys.exit("Failed to connect to Deephaven after 5 attempts")

script = """
from deephaven.TableTools import emptyTable

tableOne = emptyTable(1).update("Index = i")
tableTwo = emptyTable(2).update("Index = i")
"""

session.run_script(script)
