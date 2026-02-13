# Store student records in a file
students = [
    {"name": "Divya", "roll_no": 1, "marks": 95},
    {"name": "keerti", "roll_no": 2, "marks": 90},
    {"name": "Asha", "roll_no": 3, "marks": 78}
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(f"{student['roll_no']}, {student['name']}, {student['marks']}\n")

print("Student records stored successfully.")
