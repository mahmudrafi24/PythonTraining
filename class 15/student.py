import mysql.connector
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management"
)
# Create a cursor object to interact with the database
cursor = conn.cursor()
# Create Table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        number VARCHAR(15) NOT NULL,
        grade VARCHAR(2) NOT NULL
    )
""")
# Function to insert a new student
def create_student(name, number, grade):
    query = "INSERT INTO students (name, number, grade) VALUES (%s, %s, %s)"
    values = (name, number, grade)
    cursor.execute(query, values)
    conn.commit()
    print("Student created successfully!")
# Function to read all students
def read_students():
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

# Function to update student by ID
def update_student(student_id, new_name, new_number, new_grade):
    query = "UPDATE students SET name=%s, number=%s, grade=%s WHERE id=%s"
    values = (new_name, new_number, new_grade, student_id)
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")
# Function to delete student by ID
def delete_student(student_id):
    query = "DELETE FROM students WHERE id=%s"
    values = (student_id,)
    cursor.execute(query, values)
    conn.commit()
    print("Student deleted successfully!")
# Example Usage
create_student("Alice", "A123", "A")
create_student("Bob", "B456", "B")
create_student("Harry", "B455", "B")

read_students()
update_student(1, "Alice Updated", "A789", "A+")
read_students()
delete_student(1)
read_students()

# Close the cursor and connection
cursor.close()
conn.close()