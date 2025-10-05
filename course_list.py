from course import Course
from range import Range
class CourseList:   
    def __init__(self, size = 6):
        self._courses = [None]*size         #static array
        self._count = 0
        self._size = size

     # ---------- INCREASE CAPACITY ----------
    def _increase_size(self):
        """doubles the size of course list"""
        new_size = self._size * 2
        new_courses = [None] * new_size

        # manually copy old data
        for i in Range (self._count):
            new_courses[i] = self._courses[i]

        self._courses = new_courses
        self._size = new_size

     # ---------- ADD COURSE ----------
    def add_course (self, course):
        """Adds a course and doubles array size automatically if full."""
        if self._count >= self._size:
            self._increase_size()
        # if we aleady have 2 courses so count =2 and index = 0,1 is full
        # we have to add new course at index 2 which is same as count 
        self._courses[self._count] = course     #self._courses[2] = course
        self._count += 1        #increases count by 1

    # ---------- REMOVE COURSE ----------
    def remove_course(self, code):
        """Removes a course by its code (uses search_course to find index)."""
        index = self.search_course(code)   # get index of the course
    
        if index == -1:                    # not found
            print(f"No course found with code '{code}'.")
            return
    
        # shift everything left manually
        for j in Range(index, self._count - 1):
            self._courses[j] = self._courses[j + 1]
    
        # last slot becomes empty
        self._courses[self._count - 1] = None
        self._count -= 1

    # ---------- SEARCH COURSE ----------
    def search_course(self, code):
        """Finds and returns index of a course by code."""
        for i in Range(self._count):
            if self._courses[i].code == code:
                print(f"Course found at index {i}.")
                return i      # return index instead of course object
        print(f"No course found with code '{code}'.")
        return -1             # return -1 if not found
    
    # ---------- DISPLAY ALL ----------
    def display_all(self):
        """Displays all stored courses."""
        if self._count == 0:
            print("No courses in the list yet.")
            return
        for i in Range(self._count):
            print(f"{i + 1}. {self._courses[i]}")       #calls str of course class
    

