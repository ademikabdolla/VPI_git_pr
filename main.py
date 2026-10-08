students=[
    {"name":"Әдемі", "group":"ВТиПО-26 А-2"},
    {"name":"Айзере", "group":"ВТиПО-26 А-1"},
    {"name":"Назым", "group":"ВТиПО-26 А-2"},
    {"name":"Айгерім", "group":"ВТиПО-26 А-1"},
]

def show_students():
    for student in students:
        print(student["name"], student["group"])

show_students()

def search_students(name):
    for student in students:
       if student["name"].lower() == name.lower():
            print("Табылды:", student["name"], student["group"])
            return
    print("Студент табылмады")

search_students("Әдемі")


def add_student(name, group):
    students.append({"name": name, "group": group})
    print("Қосылды:", name, group)

add_student("Сымбат", "ВТиПО-26 А-2")
show_students()