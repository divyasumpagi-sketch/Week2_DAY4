# Read student records from the file
with open("students.txt", "r") as file:
    data = file.readlines()

print("Student Records:")
for line in data:
    print(line.strip())
