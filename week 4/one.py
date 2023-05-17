import sqlite3  
conn = sqlite3.connect("employees.db")
conn.execute("Create table employees(employee_ID int primary key not null, first_name text not null, last_name text not null, email text not null, phone_number int not null, hire_date int not null, job_id text not null, salary int not null, comission int not null, manager_id text not null, deptartment_id text not null)")


conn.execute("insert into employees values(1251,'arun','kumar','ak2342@gmail.com','6734524412','2002','analyst','80000','3000','3243','engineer')")
conn.execute("insert into employees values(1259,'abhishek','gupta','ag78@yahoo.mail','8946352322','2008','receptionist','20000','1000','2453','admistration')")
conn.execute("insert into employees values(1301,'payel','dasgupta','payal@gmail.com','9134256266','2010','lawyer','80400','5000','2867','legal')")

rs = conn.execute("select first_name, last_name from employees where salary>25000")
for row in rs:
  print(row[0]," ", row[1]," ")

