lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

homework = {}
quizzes = {}
testes = {}

def get_class_average (class_list):
  results = []
  
  for a in class_list:
  	results.append(get_average(a))
    
  return average (results)  
  
def get_letter_grade (score):
  if (score >= 90):
    return "A"
  elif (score >= 80):
    return "B"
  elif (score >= 70):
    return "C"
  elif (score >= 60):
    return "D"
  else:
    return "F"
  

def get_average (student):
  homework = {student["name"] : average(student["homework"])}
  quizzes = {student["name"] : average(student["quizzes"])}
  tests = {student["name"] : average(student["tests"])}

  return homework[student["name"]] * 0.1 + quizzes[student["name"]] * 0.3 + tests[student["name"]] * 0.6

def average(numbers):
  sum = 0
  for s in numbers:
    sum += s

  return float(sum)/float(len(numbers))

print (get_letter_grade(get_average (lloyd)))
print (get_letter_grade(get_average (alice)))
print (get_letter_grade(get_average (tyler)))
print (get_class_average(students))
