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
# US3: Find a list of businesses of a particular price range that offer discounts to dashpass users.
#------------------------------------------------------------

def get_discount_business(price_range):
    tmpl = '''
        SELECT b.name, b.cuisine, d.discount_pct
          FROM Business as b JOIN Discount as d ON b.id = d.business_id
         WHERE (price_range = %s and d.is_dashpass = TRUE and EXISTS (SELECT business_id FROM Discount)); 
    '''
    cmd = cur.mogrify(tmpl, (price_range))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['business name', 'price range', 'discount'])
    for row in rows:
        table.add_row(row)
    print('#US3 (customer-complex): Finding a list of businesses of a particular price range that offer discounts to dashpass users.')
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


get_discount_business('2')
get_discount_business('1')