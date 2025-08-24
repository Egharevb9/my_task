# created empty list for student names and empty list for student_score
student_names = []
student_score = []
try:
    # asking user for student name and adding users input into te empty list called student_names
    for i in range(3):
        name = input(f"Enter the nmber {i + 1} student name: ")
        student_names.append(name)


    # collecting student scores adding users input into te empty list called student_score
    for name in student_names:
        score = int(input(f"Enter {name} score: "))
        student_score.append(score)

    # Storing data in a dictionary 
    students = {name: score for name, score in zip(student_names, student_score)}

    # output
    for key, value in students.items():
        print(f"{key} score is {value}")
except ValueError:
    print("Invalid input")
finally:
    print("Program closed")
