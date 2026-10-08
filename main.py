students=[
    {"name":"Әдемі", "group":"ВТиПО-26 А-2"},
    {"name":"Айзере", "group":"ВТиПО-26 А-1"},
    {"name":"Назым", "group":"ВТиПО-26 А-2"},
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