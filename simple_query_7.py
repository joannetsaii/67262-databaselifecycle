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
# US7: Insert incoming orders into the system
#------------------------------------------------------------

def insert_order(id, date, price, customer_id, business_id, driver_id, discount_id, rating):
    tmpl = '''
        INSERT INTO "Order"(id, date, price, customer_id, business_id, driver_id, discount_id, rating)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (id, date, price, customer_id, business_id, driver_id, discount_id, rating))
    print_cmd(cmd)
    cur.execute(cmd)
    print('#US7 (business-simple): Inserting incoming orders into the system.\nInserted result is shown in table Order when run show_all.')
    # print(table)

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
#result is displayed when run show_all (order added to Order table)
insert_order(262, '2022/10/10', 2, 6, 5, 11, 112, None)