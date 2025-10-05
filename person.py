class Person:
    def __init__ (self, name, email, age, gender):
        self._name = self._validate_name(name)
        self._email = self._validate_email(email)
        self._age = self._validate_age(age)
        self._gender = self._validate_gender(gender)

    # ---------- HELPER FUNC ----------

    def _validate_name(self, name):
        if not isinstance (name , str):
            raise TypeError ("name should be string")
        if not name.strip():
            raise ValueError("name cannot be empty")
        return name.strip()
        
    def _validate_email(self, email):
        """Checks if email has a basic valid format."""
        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            return email
        else:
            raise ValueError("Invalid email format.")
    
    def _validate_age (self, age):
        if not isinstance (age, int):
            raise TypeError ("age should be a number")
        if age <= 0:
            raise ValueError ("age must be positive")
        return age
    
    def _validate_gender(self,gender):
        gender = gender.lower()
        if gender != "male" and gender != "female":
            raise ValueError("gender can only be male or female")
        return gender
    
    # ---------- PROPERTY ----------
    @property
    def name (self):
        return self._name
    @name.setter
    def name (self,name):
        self._name = self._validate_name(name)

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email= self._validate_email(email)

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age= self._validate_age(age)

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self,gender):
        self._gender= self._validate_gender(gender)

     # ---------- DISPLAY ----------

    def display_info(self):
        """Prints all basic info in a neat format."""
        print("----- PERSON INFO -----")
        print(f"Name   : {self._name}")
        print(f"Email  : {self._email}")
        print(f"Age    : {self._age}")
        print(f"Gender : {self._gender}")
        print("------------------------")

    def __str__(self):
        return f"Name: {self._name}, Email: {self._email}, Age: {self._age}, Gender: {self._gender}"


