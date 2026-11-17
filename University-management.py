class Person:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

class Student(Person):
    def __init__(self, name, age, course, roll_number, marks):
        super().__init__(name, age, course)
        self.roll_number = roll_number
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def update_marks(self, mrks):
        self.__marks = mrks

    def show_student_information(self):
        print(f"The name is {self.name}")
        print(f"Age of student is {self.age}")
        print(f"course is {self.course}")
        print(f"Roll number is {self.roll_number}")
        print(f"Marks is ", self.get_marks())    

class Teacher(Person):
    def __init__(self, name, age, course, salary, status):
        super().__init__(name, age, course)
        self.__salary = salary
        self.status = status

    def get_salary(self):
        return self.__salary
    def update_salary(self,salry):
        self.__salary=salry

    def show_teacher_information(self):
        print(f"The name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Course is {self.course}")
        print(f"Status is {self.status}")
        print(f"Salary is ", self.get_salary())

class Graduate_student(Student):
    def __init__(self, name, age, course, roll_number, marks, session):
        super().__init__(name, age, course, roll_number, marks)
        self.session = session

    def get_marks(self):
        return super().get_marks()

    def update_marks(self,mrks):
        super().update_marks(mrks)

    def show_graduate_student_information(self):
        print(f"Name is {self.name}")
        print("A graduate student")
        print(f"Course is {self.course}")
        print(f"Age is {self.age}")
        print(f"Roll number is {self.roll_number}")
        print(f"Session is {self.session}")
        print(f"Marks are ", self.get_marks())

class teacher_assistant(Student,Teacher):
    def __init__(self, name, age, course, roll_number, marks, salary, status):
        Person.__init__(self, name, age, course)
        self.roll_number = roll_number
        self._Student__marks = marks
        self._Teacher__salary = salary
        self.status = status

    def show_teacher_assistant_information(self):
        print(f"Student name is {self.name}")
        print(f"Student age is {self.age}")
        print(f"Student course is {self.course}")
        print(f"Student roll number is {self.roll_number}")
        print(f"Student marks are", self.get_marks())
        print(f"Student is {self.status}")
        print(f"Student salary is", self.get_salary())

student1=Student("Muhammad Hanzala", 21, "Computer Science", 3, 1155)
student1.update_marks(1156)
student1.show_student_information()
print('--------------')
teacher1=Teacher("Muhammad Ali", 27, "OOP", 75000, "visiting")
teacher1.update_salary(78000)
teacher1.show_teacher_information()
print('--------------')
stdteacher1=teacher_assistant("Muhammad Rizwan", 23, "Programming", 18, 1092, 48000, "visiting")
stdteacher1.show_teacher_assistant_information()
print("--------------")
student2=Graduate_student("Noor Fatima", 19, "Database", 12, 1098, "2026-2030")
student2.show_graduate_student_information()
