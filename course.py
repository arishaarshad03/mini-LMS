class Course:
    def __init__(self, name, code, credit_hour):
        self._name = self._validate_name(name)
        self._code = self._validate_course_code(code)
        self._credit_hour = self.validate_credit_hour(credit_hour)

    # ---------- HELPER FUNC ----------
    def _validate_name(self, name):
        if not isinstance (name, str):
            raise TypeError ("course name should be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")
        return name.strip()
    
    def _validate_course_code(self, code):
        if not isinstance(code, str):
            raise TypeError("Course code must be a string.")
        code = code.strip().upper()
        if not code:
            raise ValueError("Course code cannot be empty.")
        if not any(ch.isalpha() for ch in code) or not any(ch.isdigit() for ch in code):
            raise ValueError("Course code must include both letters and numbers.")
        return code
    
    def validate_credit_hour(self, credit_hour):
        if not isinstance (credit_hour, int):
            raise TypeError("credit hour must be an integer")
        if credit_hour <= 0 or credit_hour > 5:
            raise ValueError("Credit hour must be between 1 and 5.")
        return credit_hour
    
    # ---------- PROPERTY ----------
    @property
    def name (self):
        return self._name
    @name.setter
    def name (self, name):
        self._name = self._validate_name(name)

    @property
    def code (self):
        return self._code
    @code.setter
    def code (self, code):
        self._code = self._validate_course_code(code)

    @property
    def credit_hour (self):
        return self._credit_hour
    @credit_hour.setter
    def credit_hour (self, credit_hour):
        self._credit_hour = self.validate_credit_hour(credit_hour)

 # ---------- DISPLAY ----------
    def display_info(self):
        """Displays all course information."""
        print("----- COURSE INFO -----")
        print(f"Course Name  : {self._name}")
        print(f"Course Code  : {self._code}")
        print(f"Credit Hours : {self._credit_hour}")
        print("------------------------")

    def __str__(self):
        return f"{self._name} ({self._code}) - {self._credit_hour} Credit Hour(s)"

    