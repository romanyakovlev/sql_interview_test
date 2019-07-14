from db_utils import db_connect
con = db_connect() # connect to the database
cur = con.cursor() # instantiate a cursor obj
cur.execute('''INSERT INTO employees(id, name, surname, salary_year)
                  VALUES(?,?,?,?)''', ('1','John','Terrible', '11000'))
cur.execute('''INSERT INTO employees(id, name, surname, salary_year)
                  VALUES(?,?,?,?)''', ('2','Maggie','Woodstock', '15000'))
cur.execute('''INSERT INTO employees(id, name, surname, salary_year)
                  VALUES(?,?,?,?)''', ('3','Joel','Muegos', '22000'))
cur.execute('''INSERT INTO employees(id, name, surname, salary_year)
                  VALUES(?,?,?,?)''', ('4','Jercen','Vab Kapl', '44000'))

cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('1', '01.01.15', '250','1'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('2', '01.02.15', '267','1'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('3', '01.01.15', '300','2'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('4', '01.02.15', '350','2'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('5', '01.01.15', '245','3'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('6', '01.02.15', '355','3'))

cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('7', '01.01.15', '246','4'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('8', '01.02.15', '356','4'))
cur.execute('''INSERT INTO taxes(id, month, taxes, employee_id)
                  VALUES(?,?,?,?)''', ('9', '01.03.15', '412','3'))
# Commit the change


cur.execute('''INSERT INTO positions(id, internal_number, position, employee_id)
                  VALUES(?,?,?,?)''', ('1', '32894', 'Manager','1'))
cur.execute('''INSERT INTO positions(id, internal_number, position, employee_id)
                  VALUES(?,?,?,?)''', ('2', '23409', 'Top Manager','2'))

cur.execute('''INSERT INTO positions(id, internal_number, position, employee_id)
                  VALUES(?,?,?,?)''', ('3', '23908', 'CEO','3'))
cur.execute('''INSERT INTO positions(id, internal_number, position, employee_id)
                  VALUES(?,?,?,?)''', ('4', '128', 'Board Chairman','4'))

con.commit()

