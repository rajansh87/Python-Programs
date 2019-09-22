import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("create table if not exists emp0135(id number primary key, ename varchar(20),esal number)")
cur.execute("insert into emp0135 values(101,'KB meena', 50000)")
a=[(102,'Ratnesh', 70000),(103,'Ajay Kr', 75000),(104,'Prateek', 72000)]
cur.executemany("insert into emp0135 values(?,?,?)",a)

cur.execute('select *from emp0135')
cur.fetchall()
cur.execute("create table if not exists emp01(id number, post varchar(20),dept varchar(20))")
cur.execute("create table if not exists emp02(id number, vehical varchar(20),house varchar(20))")
cur.execute("insert into emp01 values(101,'lecturer','CSE')")
cur.execute("insert into emp01 values(102,'Sr lecturer','CSE')")
cur.execute("insert into emp02 values(101,'Swift','ATS-2E65')")
cur.execute("insert into emp02 values(102,'Swift Dezire','ATS-2C25')")






