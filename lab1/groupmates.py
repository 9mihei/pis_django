# -*- coding: utf-8 -*-

groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print("Имя студента".ljust(15),
          "Группа".ljust(8),
          "Возраст".ljust(8),
          "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["group"].ljust(8),
              str(student["age"]).ljust(8),
              str(student["marks"]).ljust(20))
    print("\n")

print_students(groupmates)
def filter_by_marks(students, min_avg):
    filtered = []
    for student in students:
        # Считаем среднюю оценку
        avg_mark = sum(student["marks"]) / len(student["marks"])
        # Если средний балл выше порога - добавляем в список
        if avg_mark > min_avg:
            filtered.append(student)
    return filtered

print("Студенты со средним баллом выше 4.0:")
good_students = filter_by_marks(groupmates, 4.0)
print_students(good_students)