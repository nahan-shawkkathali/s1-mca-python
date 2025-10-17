student={"name":"nahan",
       "roll number":45,
       "register number":19860,
       "department":"MCA",
       "semester":1}
student["total_mark"]=63
marks = student["total_mark"]
if marks >= 90:
    grade = "A"
elif marks >= 82:
    grade = "B"
elif marks >= 75:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "P"
else:
    grade = "F"
student["grade"] = grade
del student["roll number"]
print(student)
