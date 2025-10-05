from student import Student 
from student_list import StudentList
from course_list import CourseList
from course import Course

# DCS office creates empty student list
dcs = StudentList()

courses = CourseList(6)
courses.add_course(Course("object oriented programming", "CS101", 4))
courses.add_course(Course("digital logic design", "CS105", 3))
courses.add_course(Course("discrete structure", "CS198", 2))
courses.add_course(Course("communication and presentation", "CS001", 1))
courses.add_course(Course("pakistan studies", "CS102", 1))
courses.add_course(Course("linear algebra", "CS160", 2))

print("\n=== All Available Courses in DCS ===")
courses.display_all()

# give admission to 3 students in department
# ahmed, ayesha, bilal

dcs.add_student(Student(1, "Ahmed", "ahmed123@gmail.com", 20, "male", courses))
dcs.add_student(Student(2, "ayesha", "ayesha03@gmail.com", 25, "female", courses))
dcs.add_student(Student(3, "bilal", "bilal@gmail.com", 22, "male", courses))

print("\nAfter adding 3 new students to DCS:")
dcs.display_all()

# a new students joins in the mid of sem
s_new = Student(4, "Sara", "sara@mail.com", 20, "female")
dcs.add_student_at(s_new, 1)  # add Sara at index 1

print("\nSara joined and was placed at index 1:")
dcs.display_all()

# DCS office search for student by name
index = dcs.search_by_name("Bilal")
print("\n")
dcs._display_search_result(index)
dcs._students[index].display_info()

# DCS office search for student by seat no.
index = dcs.search_by_seat(2)
print("\n")
dcs._display_search_result(index)
dcs._students[index].display_info()

# old student is replaced by new student
s_replace = Student(5, "Ali", "ali@mail.com", 22, "male")
dcs.update_student(3 , s_replace)

print("\nrecord updated for seat 3 (bilal replaced by ali)")
dcs.display_all()

# the student leaves the department (remove)
dcs.remove_student(2)

print("\nAyesha (seat no:1) left department ")
dcs.display_all()


# check status of list
dcs.status()
