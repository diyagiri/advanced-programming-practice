import sqlite3
conn = sqlite3.connect("movie.db")
conn.execute("Create table movie(Movie_ID int primary key not null,Movie_Name text not null, genre text not null,language text null, rating int not null)")

conn.execute("insert into movie values(1001,'shutter island','mystery','english',10)")
conn.execute("insert into movie values(102,'little women','drama','english',3)")
conn.execute("insert into movie values(1030,'the notebook','romance','english',8)")
conn.execute("insert into movie values(124,'oceans 8','comedy','english',2)")



conn.execute("Delete from movie where Movie_ID=102 ")


rs = conn.execute("select * from movie")
for row in rs:
    print(row[0]," ",row[1]," ",row[2], " ",row[3]," ",row[4]," ")

print(" ")

rs= conn.execute("select * from movie where rating>3")
for row in rs:
    print(row[0]," ",row[1]," ",row[2], " ",row[3]," ",row[4]," ")  
