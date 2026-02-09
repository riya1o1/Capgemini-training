try:
    name = input("Enter student name : ")
    course_selected = int(input("Enter no.of courses selected : "))
    max_allowed = int(input("Enter max no.of courses allowed : "))
    if max_allowed < course_selected :
        raise Exception ("Course limit exceeded.")
    else:
        print("Course enrolled.")
except ValueError:
    print("Invalid input.")
except Exception as e:
    print(e)
finally:
    print("Enrollment process completed.")