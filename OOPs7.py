class Student:
    def __init__(self, stdid, stdname, college):
        self.stdid = stdid
        self.stdname = stdname
        self.college = college

    def display(self):
        print(self.stdid, self.stdname, self.college)


class standerd(Student):
    def __init__(self, stdid, stdname, college, standerd, Division):
        super().__init__(stdid, stdname, college)
        self.standerd = standerd
        self.Division = Division

    def display_standerd(self):
        self.display()
        print(self.standerd, self.Division)


class subject(Student):
    def __init__(self, stdid, stdname, college, Phy, Maths, Chem):
        super().__init__(stdid, stdname, college)
        self.Phy = Phy
        self.Maths = Maths
        self.Chem = Chem

    def display_subject(self):
        self.display()
        print(self.Phy, self.Maths, self.Chem)


stud = standerd(101, "Ali", "MHS", "11th", "D")
stud.display_standerd()

print("---------------")

sub = subject(101, "Ali", "MHS", "Physics", "Maths", "Chemistry")
sub.display_subject()

















class Student:
    def __init__(self, stdid, stdname, college):
        self.stdid = stdid
        self.stdname = stdname
        self.college = college


class Standard(Student):
    def __init__(self, stdid, stdname, college, standard, Division):
        super().__init__(stdid, stdname, college)

        self.standard = standard
        self.Division = Division


class Subject(Student):
    def __init__(self, stdid, stdname, college, Phy, Maths, Chem):
        super().__init__(stdid, stdname, college)

        self.Phy = Phy
        self.Maths = Maths
        self.Chem = Chem


# Standard object
S = Standard(
    101,
    "Danish",
    "ABC College",
    "12th",
    "A"
)

print("Student ID:", S.stdid)
print("Student Name:", S.stdname)
print("College:", S.college)
print("Standard:", S.standard)
print("Division:", S.Division)


print("\nSubject Details")

# Subject object
Sub = Subject(
    101,
    "Danish",
    "ABC College",
    "Physics",
    "Mathematics",
    "Chemistry"
)

print("Student ID:", Sub.stdid)
print("Student Name:", Sub.stdname)
print("College:", Sub.college)
print("Physics:", Sub.Phy)
print("Maths:", Sub.Maths)
print("Chemistry:", Sub.Chem)