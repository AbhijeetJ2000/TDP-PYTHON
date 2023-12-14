import mysql.connector
mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Abhijeet@123'
        )
cur = mydb.cursor()

# creating database
cur.execute("CREATE DATABASE db1")
cur.execute("use db1")

# creating table
s = "CREATE TABLE STUDENT(student_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50),  age INT, grade FLOAT)"
cur.execute(s)

# Inserting the record
cur.execute(
    "INSERT INTO STUDENT(first_name, last_name, age, grade) VALUES(%s, %s, %s, %s)", ("Alice", "Smith", 18, 95.5)
)
mydb.commit()

# Update the record
cur.execute("UPDATE STUDENT SET grade=%s WHERE first_name=%s", (97.0, "Alice"))
mydb.commit()

# Delete the record
cur.execute("DELETE FROM STUDENT WHERE last_name=%s", ("Smith",))
mydb.commit()

# fetch and display all the records
cur.execute("SELECT * FROM STUDENT")
students = cur.fetchall()
print("\nStudent Records:")
for student in students:
    print(student)


