student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for b in student_scores:
  score = student_scores[b]
  if 91 <= student_scores[b] <= 100:
    student_scores[b] = str("Outstanding")
  elif 81 <= student_scores[b] <= 90:
    student_scores[b] = str("Exceeds Expectations")
  elif 71 <= student_scores[b] <= 80:  
    student_scores[b] = str("Acceptable")
  elif student_scores[b] <= 70:
    student_scores[b] = str("Fail")
  else:
    break
  student_grades.update(student_scores)
  
  
# 🚨 Don't change the code below 👇
print(student_grades)





