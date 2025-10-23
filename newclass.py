class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


#adding students
s1 = Student("cat", 19, 60)
s2 = Student("rat", 20, 75)
s3 = Student("bat", 18, 68)

course = Course("Physics", 2)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)

print(course.add_students(s3))