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
# US4: See my monthly total revenue
#------------------------------------------------------------

def see_monthly_revenue(id, year, month):
    tmpl = '''
        SELECT b.id, b.name, sum(o.price)
          FROM "Order" as o JOIN Business as b ON b.id = o.business_id
          WHERE b.id = %s and (EXTRACT (YEAR FROM o.date) = %s) and (EXTRACT (MONTH FROM o.date) = %s)
         GROUP BY b.id, b.name
    '''
    cmd = cur.mogrify(tmpl, (id, year, month))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['business id', 'business name', 'revenue'])
    print('#US4 (business-analytical): Seeing my revenue in a given year and month.')
    for row in rows:
        table.add_row(row)
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


see_monthly_revenue('4', '2021', '12')
see_monthly_revenue('1', '2021', '12')