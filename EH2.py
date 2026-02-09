try:
    student_id = input("Enter student ID: ")
    if not student_id.isdigit() or len(student_id) != 6:
        raise Exception("Invalid Student ID")
    print("Student ID accepted")
except Exception as e:
    print(e)
