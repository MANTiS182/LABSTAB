groupmates = [
    {
        "name": "Yuri",
        "surname": "Tabakov",
        "exams": ["Math", "Physics", "Sport"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Ivan",
        "surname": "Baygushev",
        "exams": ["History", "Math", "English"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Kirill",
        "surname": "Kasimov",
        "exams": ["Philosophy", "Programming", "Math"],
        "marks": [5, 5, 2]
    },
    {
        "name": "Annastasia",
        "surname": "Malinovskay",
        "exams": ["Math", "Physics", "English"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Nikita",
        "surname": "Mitin",
        "exams": ["Programming", "Math", "Physics"],
        "marks": [5, 4, 5]
    }
]
def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(30), "Оценки".ljust(20))

    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20)
        )
def average_mark(marks):
    return sum(marks) / len(marks)
def filter_students(students, min_avg):
    result = []

    for student in students:
        avg = average_mark(student["marks"])

        if avg > min_avg:
            result.append(student)

    return result
print_students(groupmates)

value = float(input("Введите минимальный средний балл: "))

filtered = filter_students(groupmates, value)

print("\nСтуденты с баллом выше", value)
print_students(filtered)
