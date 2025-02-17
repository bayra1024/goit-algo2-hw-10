from typing import List, Dict, Set
from dataclasses import dataclass


# Визначення класу Teacher
class Teacher:
    first_name: str
    last_name: str
    age: int
    email: str
    can_teach_subjects: Set
    assigned_subjects: List

    def __init__(self, p_teacher: List):
        self.first_name = p_teacher[0].split()[0]
        self.last_name = p_teacher[0].split()[1]
        self.age = p_teacher[1]
        self.email = p_teacher[2]
        self.can_teach_subjects = p_teacher[3]
        self.assigned_subjects = []


def create_schedule(subjects, teachers):
    sorted_teachers = sorted(teachers, key=lambda x: (x[1], len(x[3])))
    print(sorted_teachers)
    result = []
    for t in sorted_teachers:
        tech = Teacher(t)
        for subj in tech.can_teach_subjects:
            if subj in subjects:
                subjects.remove(subj)
                tech.assigned_subjects.append(subj)
        result.append(tech)

    if subjects:
        return None
    return result


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        ["Олександр Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}],
        ["Марія Петренко", 38, "m.petrenko@example.com", {"Хімія"}],
        [
            "Сергій Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ],
        ["Наталія Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}],
        [
            "Дмитро Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ],
        ["Олена Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}],
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
