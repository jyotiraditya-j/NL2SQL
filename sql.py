import sqlite3

#connect to sqlite

connection=sqlite3.connect('students.db')

#create a cursor object to insert,create table,retrieve etc
cursor=connection.cursor()

# #create table
# table_info="""

# create table student(name varchar(15),class varchar(10),section varchar(5),marks int);




# """

# cursor.execute(table_info)

# #insert some more records

# cursor.execute('''insert into student values('Aditya','NLP','S',92)''')
# cursor.execute('''insert into student values('Rahul','CS','A',87)''')
# cursor.execute('''insert into student values('Tanvi','CV','B',71)''')
# cursor.execute('''insert into student values('Prerna','ECE','C',69)''')

# #display the ecords
# print("Displaying all Records")

data=cursor.execute('''SELECT * FROM student''')

for row in data:
    print(row)

connection.commit()
connection.close()


