from db_utils import db_connect
con = db_connect() # connect to the database
cur = con.cursor() # instantiate a cursor obj
employees_sql = """
    CREATE TABLE employees (
    id integer PRIMARY KEY,
    name text NOT NULL,
    surname text NOT NULL,
    salary_year integer NOT NULL)
"""
cur.execute(employees_sql)
taxes_sql = """
    CREATE TABLE taxes (
    id integer PRIMARY KEY,
    month date NOT NULL,
    taxes integer NOT NULL,
    employee_id integer NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id))
"""
cur.execute(taxes_sql)
positions_sql = """
    CREATE TABLE positions (
    id integer PRIMARY KEY,
    internal_number integer NOT NULL,
    position text NOT NULL,
    employee_id integer NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id))
"""
cur.execute(positions_sql)
result_db_sql = """
    CREATE TABLE result_db (
    internal_number integer NOT NULL,
    name_surname text NOT NULL,
    position text NOT NULL,
    salary_month integer NOT NULL,
    taxes integer NOT NULL,
    month date NOT NULL)
"""
cur.execute(result_db_sql)
