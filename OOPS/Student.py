class Student:
    def __init__(self, name, rn, yoj, courses, fees):
        self.__name = name.upper()
        self.roll_no = rn
        self.year_of_joining = yoj
        self.course = courses
        self.fees = fees

    def get_details(self, ):
        print("Student Name:", self.__name)
        # print("student public Name: ", self.name)
        print("roll Number:", self.roll_no)
        print("------------------------------")

    @staticmethod
    def welcome_msg():
        print("Hello Student, This is your Details")

    @classmethod
    def create_student_via_dob(cls, name):
        stu = cls(name, 19, 2016, "B.tech", 19000)
        return stu


s2 = Student.create_student_via_dob("Ali")
s1 = Student("mohammed Ali", 13, 2019, "MTech", 12000)
s2.get_details()
