class Person:
    base_salary = 10
    """Thuoc tinh = attributes = properties"""
    def __init__(self, name, email, age, skills):
        self.name = name
        self.email = email
        self.age = age
        self.skills =  skills
        self.loginAttempt = 0
    def login(self):
        self.loginAttempt = self.loginAttempt + 1
    def reset_login(self):
        print("Sap reset login")
        self.loginAttempt = 0
    def to_string(self):
        return "name={}, email={}, age={}, \
            skills={}, loginAttempt={}, base salary = {}"\
        .format(self.name, self.email, \
        self.age, self.skills, self.loginAttempt, self.base_salary)
    def __repr__(self):
        return "name={}, email={}, age={}, skills={}"\
        .format(self.name, self.email, \
        self.age, self.skills)