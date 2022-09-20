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
# US8: Get the average rating of all drivers who have driven for me
#------------------------------------------------------------

def avg_driverRating(id):
    tmpl = '''
       SELECT d.name, trunc(avg(o.rating), 2), b.name
       FROM Driver as d
            JOIN "Order" AS o ON d.id = o.driver_id
            JOIN Business AS b ON b.id = o.business_id 
       WHERE b.id = %s
       GROUP BY d.name, b.name
       ORDER BY b.name ASC
    '''
    cmd = cur.mogrify(tmpl, (id))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['driver name', 'average rating','business'])
    for row in rows:
        table.add_row(row)
    print('#US8 (business-complex): Getting the average rating of all drivers who have driven for a business.')
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

avg_driverRating('5')
avg_driverRating('3')