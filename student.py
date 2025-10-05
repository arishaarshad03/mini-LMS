from person import Person
from course_list import CourseList

class Student(Person):
    def __init__(self, seat_no, name, email, age, gender, course_list = None):
        super().__init__(name, email, age, gender)
        self._seat_no = self._validate_seat_no(seat_no)

        # Aggregation: student has a CourseList, but it can exist independently
        if course_list is not None:
            self._course_list = course_list
        else:
            self._course_list = CourseList()

    # ---------- VALIDATION ----------
    def _validate_seat_no(self, seat_no):
        if not isinstance (seat_no, int):
            raise TypeError("seat number should be number")
        if seat_no <= 0:
            raise ValueError("seat number can't be negative or 0")
        return seat_no
    
     # ---------- PROPERTY ----------
    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, seat_no):
        self._seat_no = self._validate_seat_no(seat_no)

    # ---------- COURSE METHODS ----------
    def add_course(self, course):
        """Adds a new course to the student's course list."""
        self._course_list.add_course(course)

    def remove_course(self, code):
        """Removes a course from the student's course list by code."""
        self._course_list.remove_course(code)

    def display_courses(self):
        """Displays all courses associated with the student."""
        self._course_list.display_all()

     # ---------- DISPLAY FUNCTION ----------
    def display_info(self):
        """Prints all student details neatly."""
        print("\n===== STUDENT INFO =====")
        print(f"Name      : {self._name}")
        print(f"Email     : {self._email}")
        print(f"Age       : {self._age}")
        print(f"Gender    : {self._gender}")
        print(f"Seat No   : {self._seat_no}")
        print("========================")
        print("Courses enrolled:")
        self.display_courses()

    def __str__(self):
        """Returns a single-line summary of the student."""
        return f"Seat No: {self.seat_no}, Name: {self.name}"