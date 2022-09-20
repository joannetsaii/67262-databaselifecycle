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
# US2: Sort the restaurants by the most amount of reviews
#------------------------------------------------------------

def sort_restaurants():
    tmpl = '''
        SELECT b.name, count(r.id)
          FROM Business as b
          JOIN Review AS r ON b.id = r.business_id
          GROUP BY b.name
         ORDER BY count(r.id) DESC
    '''
    cur.execute(tmpl)
    rows = cur.fetchall()
    table = PrettyTable(['business name', 'amount of reviews'])
    for row in rows:
        table.add_row(row)
    print('#US2 (customer-analytical): Sorting the restaurants by the most amount of reviews.')
    print(table)

if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'doordash', 'isdb'
        if len(sys.argv) >= 2:
            db = sys.argv[1]
        if len(sys.argv) >= 3:
            user = sys.argv[2]
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))

#example
sort_restaurants()