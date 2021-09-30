student_scores = {
    "Harry": 81,  # exeeds
    "Ron": 78,  # accept
    "Hermione": 99,  # outstand
    "Draco": 74,  # accept
    "Neville": 62,  # Fail
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
grade = ""
# TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    # check to see what grade the student got
    if 0 <= student_scores[i] <= 70:
        grade = "Fail."
    elif 71 <= student_scores[i] <= 80:
        grade = "Acceptable"
    elif 81 <= student_scores[i] <= 90:
        grade = "Exceeds Expectations"
    elif 91 <= student_scores[i] <= 100:
        grade = "Outstanding"
    else:
        grade = "invalid grade, grade much be within the range 0-100"
    # Write grade to grade dictionary
    student_grades[i] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
