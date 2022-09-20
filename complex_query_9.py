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
# US9: Check what possible rewards I can get with my current doordash points
#------------------------------------------------------------

def rewards_withPoints(id):
    tmpl = '''
       SELECT c.id, c.name, r.reward
       FROM Customer as C
            LEFT JOIN Exchange AS e ON c.id = e.customer_id
            LEFT JOIN Reward AS r ON e.reward_id = r.id
       WHERE (c.id = %s and c.points >= r.points_needed)
       ORDER BY c.name ASC
    '''
    cmd = cur.mogrify(tmpl, (id))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['customer id', 'customer name', 'reward'])
    for row in rows:
        table.add_row(row)
    print('#US9 (customer-complex): Checking what possible rewards a customer can get with his/her current doordash points.')
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

rewards_withPoints('5')
rewards_withPoints('9')
