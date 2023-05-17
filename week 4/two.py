import sqlite3
conn = sqlite3.connect("worker.db")
conn.execute("Create table work(worker_id int primary key not null,fname text not null, lname text not null,salary int not null, j_date text not null,dept text not null)") 

conn.execute("insert into work values(104,'raj','ganesh',55000,'19-02-2000','cse')")
conn.execute("insert into work values(105,'adam','levi',13000,'10-02-2000','cse')")
conn.execute("insert into work values(106,'rajes','kumar',340000,'12-02-2000','cse')")
conn.execute("insert into work values(107,'arun','kumar',99500,'9-02-2000','Administration')")
conn.execute("insert into work values(1251,'arun','surendar',63000,'12-03-2000','eee')")
conn.execute("insert into work values(129,'abhishek','kumar',9000,'20-02-2000','Administration')")
conn.execute("insert into work values(199,'harsh','kumar',9000,'20-02-2000','Administration')")
conn.execute("insert into work values(131,'chandru','surya',270000,'1-06-2000','eee')") 
conn.execute("insert into work values(180,'payal','das',34000,'15-03-2000','Administration')")
conn.execute("insert into work values(147,'apala','pal',99500,'9-01-2000','cse')")
conn.execute("insert into work values(1282,'depak','roy',63300,'2-03-2000','eee')")

rs = conn.execute("select fname as Worker_name from work")
for row in rs:
  print(row[0])

rs = conn.execute("select upper(fname) from work")
for row in rs:
  print(row[0])

rs= conn.execute("select distinct dept from work")
for row in rs:
  print(row[0])

rs= conn.execute("select * from work order by fname")
for row in rs:
  print(row[0]," ",row[1]," ",row[2])

rs= conn.execute("select * from work where fname not in ('raj','arun')")
for row in rs:
  print(row[0]," ",row[1]," ",row[2])

rs= conn.execute("select * from work where salary between 10000 and 50000")
for row in rs:
  print(row[0]," ",row[1]," ",row[2]," ",row[3])

rs= conn.execute("select max(salary) from work")
for row in rs:
  print(row[0])

rs=  conn.execute("select avg(salary) as Avg_Sal from work")
for row in rs:
  print(row[0])

#rs= conn.execute(" select left(fname, 3) from work (Select SUBSTRING(fname,1,3) from work)") 
#for row in rs: 
#  print(row[0])

#rs= conn.execute("select instr(fname, binary'a') from work where fname = 'adam';")
#for row in rs:
#  print(row[0])

rs= conn.execute("select distinct length(dept) from work;")
for row in rs:
  print(row[0])

rs= conn.execute("select * from work where fname like '____h';")
for row in rs:
  print(row[0], row[1], row[2], row[3], row[4], row[5])

rs= conn.execute("select count(*) from work where dept = 'Administration';")
for row in rs:
  print(row[0])


