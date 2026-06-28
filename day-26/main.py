import random
import pandas

numbers = [1,2,3]
new_list = [number + 1 for number in numbers]
print(new_list)

name = "Dinda"
new_letters = [letter for letter in name]
print(new_letters)

new_ranges = [num * 2 for num in range(1,5)]
print(new_ranges)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score > 50 }
print(passed_students)

students_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)

# Pandas build-in loop

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)