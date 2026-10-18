
# Hybrid Inheritance

class Person:
    def __init__(self, pname, gender, age, **kwargs):
        super().__init__(**kwargs)
        self.pname = pname
        self.gender = gender
        self.age = age


class Sports(Person):
    def __init__(self, sport, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport

    def display(self):
        print("----- Sports Details -----")
        print("Person Name :", self.pname)
        print("Gender      :", self.gender)
        print("Age         :", self.age)
        print("Sport       :", self.sport)


class Academics(Person):
    def __init__(self, education, **kwargs):
        super().__init__(**kwargs)
        self.education = education


class Skills(Person):
    def __init__(self, skill, **kwargs):
        super().__init__(**kwargs)
        self.skill = skill


class Job(Academics, Skills):
    def __init__(self, pname, gender, age, education, skill):
        super().__init__(pname=pname,gender=gender,age=age,education=education,skill=skill)

    def display(self):
        print("----- Job Details -----")
        print("Person Name :", self.pname)
        print("Gender      :", self.gender)
        print("Age         :", self.age)
        print("Education   :", self.education)
        print("Skills      :", self.skill)


j1 = Job("Ali", "Male", 24, "B.Tech", "Python, Java, C++")
j1.display()

print()

S = Sports("Cricket", pname="Ali", gender="Male", age=24)
S.display()
