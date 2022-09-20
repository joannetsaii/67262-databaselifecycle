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
# US5: See my weekly earnings on a given week
#------------------------------------------------------------

def get_yearly_earnings(id, year): #driver_id
                                   #we assume that a dasher earns $5 per delivery
    tmpl = '''
        SELECT driver_id, 5*count(id)
          FROM "Order"
         WHERE driver_id = %s and EXTRACT (YEAR FROM date) = %s
         GROUP BY driver_id
    '''
    cmd = cur.mogrify(tmpl, (id, year))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['driver id', 'earnings'])
    for row in rows:
        table.add_row(row)
    print('#US5 (driver-analytical): Seeing my earnings in a given year. According to the policies of Doordash, we assume that the driver earns $5 per delivery.')
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

#examples
get_yearly_earnings(11, '2021')
get_yearly_earnings(12, '2021')