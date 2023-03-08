from main import Student

try:
    student_name = input("enter your name\n")
    student_id = input("enter your id\n")
    student_class = input("enter your class\n")

    Student.create_table(student_name= student_name, student_id=student_id, student_class=student_class)
    print("user created successfully")

except:
    print("failed")
