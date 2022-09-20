#-----------------------------------------------------------------
# Working with psycopg2
#-----------------------------------------------------------------

import psycopg2
import sys
from prettytable import PrettyTable

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)

    
#------------------------------------------------------------
# US1: Filter cuisine and price to select a restaurant
#------------------------------------------------------------

def filter_business(cuisine, price_range):
    tmpl = '''
        SELECT cuisine, price_range, name
          FROM Business
         WHERE cuisine = %s and price_range = %s
         ORDER BY cuisine
    '''
    cmd = cur.mogrify(tmpl, (cuisine, price_range))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['cuisine', 'price range', 'business name'])
    for row in rows:
        table.add_row(row)
    print('#US1 (customer-simple): Filtering cuisine and price to select a restaurant.')
    print(table)

if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'doordash', 'isdb'
        # you may have to adjust the user 
        # python a4-socnet-sraja.py a4_socnet postgres
        if len(sys.argv) >= 2:
            db = sys.argv[1]
        if len(sys.argv) >= 3:
            user = sys.argv[2]
        # by assigning to conn and cur here they become
        # global variables.  Hence they are not passed
        # into the various SQL interface functions
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))

#example1
filter_business("asian", 2)
#example2
filter_business("mexican", 2)