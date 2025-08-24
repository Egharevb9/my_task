# collecting users name and age
student = {}
user_name = input("enter your name: ")
user_age =int(input("enter your age: "))

# updating the student data
student.update({"name": user_name, "age":user_age})

score =[70, 80, 90]
student["score"] = score
# calculating average score
average_score = sum(score)/len(score)

# checking for pass or fail
passed_student = average_score >= 50
if average_score >= 50:
    student["result"] = "Pass"
else:
    student["result"] = "Fail"

# checking if student is a teenager or not
teenager = (user_age >=13) and (user_age <=19)
if user_age >=13 and user_age <= 19:
    student["teenager"] = "yes"
else:
    student["teenager"] = "no"
print(f"\nStudent Record:\nName: {student["name"]}\nAge: {student["age"]}\nscore: {student["score"]}\nResult: {student["result"]}\nTeenager: {student["teenager"]}")