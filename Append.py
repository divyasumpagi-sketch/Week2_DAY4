# Append new student data to the file
new_student = {"name": "David", "roll_no": 4, "marks": 88}

with open("students.txt", "a") as file:
    file.write(f"{new_student['roll_no']}, {new_student['name']}, {new_student['marks']}\n")

print("New student record appended successfully.")
