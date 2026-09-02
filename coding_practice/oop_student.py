# Make a student class storing name and a list of grades,
# with a method to compute the average.

# creating Student class
class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = list(grades)

    # creating method() that compute the average
    def grade_average(self):
        return (sum(self.grades)/ len(self.grades))

# creating an instane
student_name = input('Please enter student\'s name:' )
grade_list = input('Please input the grades for the student, separated by coma:' )
grade_list = [int(g.strip()) for g in grade_list.split(',')]

student= Student(student_name, *grade_list)
student.grade_average()
print(f"The student, {student.name}, had an average score of {student.grade_average()}")


