from db_utils import db_connect
con = db_connect() # connect to the database
cur = con.cursor() # instantiate a cursor obj
employees_sql = """
    INSERT into result_db (internal_number,name_surname,position,salary_month,taxes,month)
    SELECT p.internal_number, (e.name || ' '  || e.surname), p.position, (salary_year/12), t.taxes, t.month
    FROM employees e 
    JOIN taxes t ON e.id = t.employee_id
    JOIN positions p ON e.id = p.employee_id
    ORDER BY e.id;
"""
cur.execute(employees_sql)
con.commit()
