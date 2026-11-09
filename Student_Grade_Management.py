students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "scores": [85,78,92]
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "scores": [65,70,68]
    },
    "S003": {
        "name": "Diana",
        "age": 19,
        "scores": [100,100,100]
    }
}
def add_student():
    name = input("Enter Student's Name: ")
    age = int(input("Enter Student's Age: "))
    scores = []
    for i in range(1, 4):
        score = int(input("Enter Student's Score"))
        scores.append(score)
        student_id = f"len(S({students}))+1:03"
        students[student_id] = {
            f"name": {name},
            f"age": {age},
            f"scores": {scores}
        }
        print("Student Added Successfully.")
def view_all_students():
    for student in students.items():
        print(student)
def search_student():
    student_id = input("Enter Student ID To Search: ").strip().capitalize()
    if student_id in students:
        print(students[student_id])
        return
    print("Not Found")
def each_student_average():
    #student_id = input("Enter Student ID: ")
    #if student_id in students:
    for student_id in students.values():
        total = sum(student_id["scores"])
        #print(f"{student_id}-Total: {total}")
        average = total/len(student_id["scores"])
        print(f"{student_id}-Average: {average: 2f}")
def all_student_average():
    grand_total = (sum(sum(student["scores"]) for student in students.values()))
    print(f"Grand Total Scores: {grand_total}")
    average = grand_total/len(students["scores"])
    print(f"Averasge Scores: {average}")
def find_best_student():
    best = max(students, key=lambda sid: students[sid]["scores"])
    print(f"{students[best]["name"]}: {students[best]["scores"]}")
def student_who_passed():
    passed = {
        student_id: sum(student["scores"])/len(student["scores"])
        for student_id, student in students.items()
        if sum(student["scores"])/len(student["scores"]) >= 50
    }
    for student_id,average in passed.items():
        print("\n====STUDENTS WHO PASSED====\n")
        print(f"{student_id}: {average:.2f}")
def perfect_scores():
    perfect = ([student["scores"] == [100,100,100] for student in students.values()])
    if not all(student["scores"] == perfect for student in students.values()):
        print("No Perfect Score Found")
        return
    print(perfect)
def update_scores():
    student_id = input("Enter student ID To Update Scores: ").strip().title()
    if not student_id in students:
        return
    print("Not Found.")    
    for i in range(1,4):
        scores = input("Enter New Scores: ")
        students[student_id]["scores"] = scores
        print("Scores Successfully Updated.")
def delete_student():
    student_id = input("Enter student ID To Delete: ")
    if not student_id in students:
        print("Not Found.")
        return
    delete = input(f"Confirm To Delete {student_id}(yes/no): ")
    if delete == "yes":
        del students[student_id]
        print(f"{student_id} Deleted Successfully.")
        return
    pass
def save_report():
    with open("student_report.txt","w") as file:
        file.write("=====STUDENT REPORT=====\n\n")
        for sid, student in students.items():
            average = sum(student["scores"])/len(student["scores"])
            file.write(f"{sid}-{student["name"]}\n")
            file.write(f"Age : {student["age"]}\n")
            file.write(f"Scores: {student["scores"]}\n")
            file.write(f"Average: {round(average,2)}\n\n")
    print("Report Saved To student_report.txt")
while True:
    print("\n=====STUDENT GRADE MANAGEMENT=====\n" \
        "1).Add Student\n" \
        "2).View All Students\n" \
        "3).Search Student\n" \
        "4).Calculate Student Average\n" \
        "5).Find Best Student\n" \
        "6).Find Student Who Passed\n" \
        "7).Show Students With Perfect Scores\n" \
        "8).Update Student Scores\n" \
        "9).Delete Student\n" \
        "10).Save Report\n" \
        "11).One Student Average\n" \
        "0).Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        all_student_average()
    elif choice == "5":
        find_best_student()
    elif choice == "6":
        student_who_passed()
    elif choice == "7":
        perfect_scores()
    elif choice == "8":
        update_scores()
    elif choice == "9":
        delete_student()
    elif choice == "10":
        save_report()
    elif choice == "11":
        each_student_average()