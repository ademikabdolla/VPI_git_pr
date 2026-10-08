students=[
    {"name":"Әдемі", "group":"ВТиПО-26 А-2"},
    {"name":"Айзере", "group":"ВТиПО-26 А-1"},
    {"name":"Назым", "group":"ВТиПО-26 А-2"},
]

def show_students():
    for student in students:
        print(student["name"], student["group"])

show_students()