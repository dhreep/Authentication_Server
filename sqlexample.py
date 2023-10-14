import sqlite3

#define conection and cursor
conn = sqlite3.connect("Servdata.sqlite")
cursor = conn.cursor()
#create table
command1 = """CREATE TABLE IF NOT EXISTS Login
(
  Username TEXT NOT NULL,
  Password TEXT NOT NULL,
  IP TEXT NOT NULL,
  Key INTEGER,
  PRIMARY KEY (Username),
  UNIQUE (IP)
)"""
cursor.execute(command1)
# Insert queries
# 1. Insert a new user with a unique IP address
query1 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user1', 'password1', '192.168.1.1', 1234);"

# 2. Insert a user with a different unique IP address
query2 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user2', 'password2', '10.0.0.1', 5678);"

# 3. Insert a user with a different unique IP address
query3 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user3', 'password3', '172.16.0.1', 9876);"

# 4. Insert a user with a different unique IP address
query4 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user4', 'password4', '192.168.1.2', 2468);"

# 5. Insert a user with a unique IP and a NULL Key
query5 = "INSERT INTO Login (Username, Password, IP) VALUES ('user5', 'password5', '192.168.1.3');"

# 6. Insert a user with a NULL Password
query6 = "INSERT INTO Login (Username, IP, Key) VALUES ('user6', '10.0.0.2', 1357);"

# 7. Insert a user with default values (NULL Key, Password)
query7 = "INSERT INTO Login DEFAULT VALUES;"

# 8. Insert a user with a long IP address
query8 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user8', 'password8', '192.168.1.4', 7777);"

# 9. Insert a user with a negative Key value
query9 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('user9', 'password9', '192.168.1.5', -1234);"

# 10. Insert a user with a very long Username and Password
query10 = "INSERT INTO Login (Username, Password, IP, Key) VALUES ('a' * 50, 'b' * 50, '192.168.1.6', 9999);"

#Execute the queries
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query5)
# cursor.execute(query6)
#cursor.execute(query7)
cursor.execute(query8)
cursor.execute(query9)
cursor.execute(query10)

cursor.execute("SELECT * FROM Login")
for row in cursor.fetchall():
    for val in row:
        print(val,"\t",type(val))

# Commit the changes and close the connection
conn.commit()
conn.close()

