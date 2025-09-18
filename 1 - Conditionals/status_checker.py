# Student Information System - Starter Code
print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
GPA = float(input("Enter student GPA (0.0-4.0): "))


# Show student information
print("")
print("Student Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {GPA}")

# TODO: Check if age is valid (between 16 and 100)
if age <= 16 or age <=100:
    print("Age must be a valid number")

# TODO: Check if GPA is valid (between 0.0 and 4.0)
if GPA > 4.0 or GPA < 0.0:
    print("GPA must be between 0.0-4.0")

print("")
print("Eligibility Status:")
# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
if age >= 18 and GPA >= 2.0:
    print("ELIGIBLE for enrollment")
else:
    print("NOT ELIGIBLE for enrollment")

# TODO: Check voting eligibility (age >= 18)
if age >= 18:
    print("ELIGIBLE to vote")
else:
    print("NOT ELIGIBLE to vote")

# TODO: Check honor roll status (gpa >= 3.5)
if GPA >= 3.5:
    print("ON HONOR ROLL")
else:
    print("NOT ON HONOR ROLL")