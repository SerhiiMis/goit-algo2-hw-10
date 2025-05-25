from typing import Set, List


class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects: Set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> List[Teacher]:
    uncovered = set(subjects)
    selected_teachers = []

    while uncovered:
        best = None
        max_cover = 0

        for teacher in teachers:
            teachable = teacher.can_teach_subjects & uncovered
            if len(teachable) > max_cover or (
                len(teachable) == max_cover and best and teacher.age < best.age
            ):
                best = teacher
                max_cover = len(teachable)

        if not best or max_cover == 0:
            return None  # 

        assign = best.can_teach_subjects & uncovered
        best.assigned_subjects = assign
        selected_teachers.append(best)
        uncovered -= assign
        teachers.remove(best)

    return selected_teachers


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for t in schedule:
            print(f"{t.first_name} {t.last_name}, {t.age} років, email: {t.email}")
            print(f"   Викладає предмети: {', '.join(t.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
