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
# US6: Count how many orders I have today 
#------------------------------------------------------------

def count_order(id, date):
    tmpl = '''
        SELECT d.id, o.date, count(o.id)
          FROM "Order" as o LEFT JOIN Driver as d ON d.id = o.driver_id
         WHERE d.id = %s and o.date = %s
         GROUP BY d.id, o.date
    '''
    cmd = cur.mogrify(tmpl, (id, date))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['driver id', 'date', 'order count'])
    for row in rows:
        table.add_row(row)
    print('#US6 (driver-analytical): Counting how many orders a driver has on a given date.')
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

#example1
count_order(13, '2021/12/25')
#example2
count_order(11, '2021/12/31')
