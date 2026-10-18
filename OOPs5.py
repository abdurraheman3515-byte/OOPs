class Personal:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Academics:
    def __init__(self, education, grade):
        self.education = education
        self.grade = grade


    


class Skills:
    def __init__(self, skillset):
        self.skillset = skillset


class Employee(Personal, Academics, Skills):
    def __init__(self, name, gender, education, grade, skillset, empid, department):
        
        Personal.__init__(self, name, gender)
        Academics.__init__(self, education, grade)
        Skills.__init__(self, skillset)

        self.empid = empid
        self.department = department


E = Employee("Danish","Male","BCA","A","Python",101,"IT")

print("Name:", E.name)
print("Gender:", E.gender)
print("Education:", E.education)
print("Grade:", E.grade)
print("Skill:", E.skillset)
print("Employee ID:", E.empid)
print("Department:", E.department)