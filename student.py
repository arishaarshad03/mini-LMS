from person import Person

class Student(Person):
    def __init__(self, seat_no, name, email, age, gender):
        super().__init__(name, email, age, gender)
        self._seat_no = self._validate_seat_no(seat_no)

    def _validate_seat_no(self, seat_no):
        if not isinstance (seat_no, int):
            raise TypeError("seat number should be number")
        if seat_no <= 0:
            raise ValueError("seat number can't be negative or 0")
        return seat_no
    
    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, seat_no):
        self._seat_no = self._validate_seat_no(seat_no)

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

    def __str__(self):
        """Returns a single-line summary of the student."""
        return f"Seat No: {self.seat_no}, Name: {self.name}"