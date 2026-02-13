# Create a new file and write data
with open("new_students.txt", "w") as file:
    file.write("Roll No, Name, Marks\n")
    file.write("1, Emma, 92\n")
    file.write("2, John, 87\n")

print("New file created and data written successfully.")
