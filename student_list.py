from student import Student
from range import Range

class StudentList:
    def __init__(self, size = 2):
        self._students = [None] * size
        self._count = 0
        self._size = size

    def _increase_size(self):
        new_size = self._size * 2
        new_students = [None] * new_size
        # copy everything in new array
        for i in Range(self._count):
            new_students[i] = self._students[i]
        self._students = new_students
        self._size = new_size

    # ---------- ADD STUDENT ----------
    def add_student(self, student):
        if self._count >= self._size:
            self._increase_size()

        # if we aleady have 2 students so count =2 and index = 0,1 is full
        # we have to add new student at index 2 which is same as count 
        self._students[self._count] = student
        self._count += 1

    def add_student_at(self, student, index):
        if index < 0 or index > self._count:
            raise IndexError("invalid index")

        if self._count >= self._size:
            self._increase_size()

        # shift elements right
        for i in Range(self._count, index, -1):
            self._students[i] = self._students[i - 1]
        self._students[index] = student
        self._count += 1

    # ---------- SEARCH ----------
    def search_by_seat(self, seat_no):
        for i in Range(self._count):
            if self._students[i].seat_no == seat_no:
                return i
        return -1

    def search_by_name(self, name):
        for i in range(self._count):
            if self._students[i].name.lower() == name.lower():
                return i
        return -1  # return -1 if no student is found

    # ---------- HELPER TO DISPLAY SEARCH RESULT ----------
    def _display_search_result(self, index):
        if index != -1:
            print(f"Student found at index {index}:")
            print(self._students[index])  # calls Student.__str__()
        else:
            print("Student not found.")
    
    # ---------- REMOVE STUDENT ----------
    def remove_student(self, seat_no):
        index = self.search_by_seat(seat_no)        #get index at which student is found
        if index == -1:
            print(f"No student found with seat number {seat_no}.")
            return
        for i in range(index, self._count - 1):
            self._students[i] = self._students[i + 1]       #moves everything to left
        self._students[self._count - 1] = None      #empties the last index
        self._count -= 1        #decrease count by 1

    #---------- UPDATE STUDENT ----------
    def update_student(self, seat_no, new_student):
        """
        Replaces the student with the given seat number with a new student.
        """
        index = self.search_by_seat(seat_no)
        if index == -1:
            print(f"No student found with seat number {seat_no}.")
            return

        old_student = self._students[index]
        self._students[index] = new_student
        return f"Student with seat number {seat_no} ({old_student.name}) replaced with {new_student.name}."

    # ---------- DISPLAY ----------
    def display_all(self):
        if self._count == 0:
            print("No students in the list yet.")
            return
        for i in range(self._count):
            print (self._students[i])     #calls str method of student


    # ---------- STATUS ----------
    def status(self):
        print(f"Total students: {self._count}, List capacity: {self._size}")