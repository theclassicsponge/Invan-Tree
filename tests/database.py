import sqlite3

conn = sqlite3.connect('shoes.db')

# create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM shoes")
# get database info:
# c.fetchall() = gets all data
# c.fetchmany(3) = gets many depending on number
# c.fetchone() = gets first in database
# c.fetchone()[0]) = gets item as a tuple

items = c.fetchall()

print("Brand " + "\tModel" + "\t\tStock Number")
print("-----" + "\t-----" + "\t\t------------")
for item in items:
    print(f"{item[0]}\t {item[1]}\t {item[2]}")

# create a table:
# c.execute("""CREATE TABLE shoes (
#         brand_name TEXT,
#         model_name TEXT,
#         stock_number INTEGER
#     )""")

# execute many at once:
# many_shoes = [
#     ('ASICS', 'PATRIOT 12', '52542504'),
#     ('ASICS', 'GEL-CONTEND 7', '52543004'),
#     ('ASICS', 'GEL-CONTEND 6 GS', '52544001'),
#     ]
# c.executemany("INSERT INTO shoes VALUES (?, ?, ?)", many_shoes)

# execute one at a time:
# c.execute("INSERT INTO shoes VALUES ('ASICS','GEL-VENTURE 8', '52543901')")

# sqlite data types:
# NULL = null value
# INTEGER = a whole number
# REAL = number with decimals
# TEXT = text
# BLOB = a blob of data i.e. files, images ...

print("Command executed!")
# Commit our command
conn.commit()

# close the connection
conn.close()
