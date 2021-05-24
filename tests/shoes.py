import sqlite3

conn = sqlite3.connect('shoes.db')

# create a cursor
c = conn.cursor()

# create_a_table:

# c.execute("""CREATE TABLE inventory (
#         brand TEXT,
#         product_name TEXT,
#         stock_number INTEGER,
#         size TEXT,
#         colour TEXT,
#         stockroom_location TEXT,
#         shopfloor_location TEXT,
#         stock_quantity INTEGER,
#         stock_description TEXT,
#         price NUMERIC,
#         img BLOB,
#         web_link BLOB,
#         category TEXT
#     )""")

# # execute many at once:
# many_shoes = [
#      ('ASICS', 'PATRIOT 12', '52542505', '11 Jnr', 'Pink', 'A4', 'Not Displayed', '0', 'Coming Soon', '35.00', 'Coming Soon', 'https://www.johnlewis.com/asics-childrens-patriot-12-riptape-running-shoes/pink-glo-white/p5337901?size=11-jnr', 'Girls Shoes, Boots & Trainers'),
#      ('ASICS', 'PATRIOT 12', '52542506', '12 Jnr', 'Pink', 'A4', 'Not Displayed', '9', 'Coming Soon', '35.00', 'Coming Soon', 'https://www.johnlewis.com/asics-childrens-patriot-12-riptape-running-shoes/pink-glo-white/p5337901?size=12-jnr', 'Girls Shoes, Boots & Trainers'),
#      ('ASICS', 'PATRIOT 12', '52542503', '13 Jnr', 'Pink', 'A4', 'Not Displayed', '0', 'Coming Soon', '35.00', 'Coming Soon', 'https://www.johnlewis.com/asics-childrens-patriot-12-riptape-running-shoes/pink-glo-white/p5337901?size=13-jnr', 'Girls Shoes, Boots & Trainers'),
#      ('ASICS', 'PATRIOT 12', '52542503', '1', 'Pink', 'A4', 'Not Displayed', '0', 'Coming Soon', '35.00', 'Coming Soon', 'https://www.johnlewis.com/asics-childrens-patriot-12-riptape-running-shoes/pink-glo-white/p5337901?size=1', 'Girls Shoes, Boots & Trainers'),
#      ]
#
#     ('ASICS', 'GEL-CONTEND 7', '52543004'),
#     ('ASICS', 'GEL-CONTEND 6 GS', '52544001'),
#     ]
# c.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", many_shoes)

c.execute("INSERT INTO inventory VALUES ('ASICS', 'GEL-CONTEND 6 GS', '52544001', '3', 'Pink', 'A3', 'B8', '0', 'Coming Soon', '40.00', 'Coming Soon', 'https://www.johnlewis.com/asics-childrens-gel-contend-6-gs-running-shoes/p4815545?size=3', 'Girls Shoes, Boots & Trainers')")

print("Command executed!")
# Commit our command
conn.commit()

# close the connection
conn.close()
