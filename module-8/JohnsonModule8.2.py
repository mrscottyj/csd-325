import json

# Step 1: Load the JSON file into a class list
with open("Student.json", "r") as f:
    students = json.load(f)


# Step 2: Function that loops through the class list and prints each value
def print_students(student_list):
    for student in student_list:
        print(student["L_Name"] + ", " + student["F_Name"] +
              " : ID = " + str(student["Student_ID"]) +
              " , Email = " + student["Email"])


# Step 4: Output notification – original list
print("This is the original Student list:")
print("-" * 50)

# Step 5: Call print function
print_students(students)

# Step 6: Append your own record to the class list
students.append({
    "F_Name": "Ellen",
    "L_Name": "Ripley",
    "Student_ID": 45604,
    "Email": "eripley@gmail.com"
})

# Step 7: Output notification – updated list
print()
print("This is the updated Student list:")
print("-" * 50)

# Step 8: Call print function
print_students(students)

# Step 9: Use json.dump() to write updated data back to the .json file
with open("Student.json", "w") as f:
    json.dump(students, f, indent=4)

# Step 10: Output notification – file updated
print()
print("The .json file was updated.")