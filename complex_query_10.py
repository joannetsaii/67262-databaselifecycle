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
# US10: Find customers who have left me a review 
#------------------------------------------------------------

def review_fromCust(id):
    tmpl = '''
       SELECT DISTINCT b.name, c.name
       FROM Customer as C
            JOIN Review AS r ON c.id = r.customer_id
            JOIN Business AS b ON r.business_id = b.id
       WHERE b.id = %s
       ORDER BY b.name ASC
    '''
    cmd = cur.mogrify(tmpl, (id))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['business name', 'customer name'])
    for row in rows:
        table.add_row(row)
    print('#US10 (business-complex): Finding customers who have left a business review.')
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

review_fromCust('1')

