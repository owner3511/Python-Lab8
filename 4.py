def make_student(name, score, group=""):
    student = {"name": name, "score": score}
    if group != "":
        student["group"] = group
    return student
students = []
while True:
    name_input = input("Name (quit to stop): ")
    if name_input.lower() == "quit":
        break
    score_input = int(input("Score: "))
    group_input = input("Tələbənin qrupu (istəyə bağlıdır, boş buraxa bilərsiniz): ")
    netice = make_student(name_input, score_input, group_input)
    students.append(netice)
for st in students:
    print(st)