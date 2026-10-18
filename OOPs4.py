class person():
    def __init__(self,name,age,gender,DOB):
        self.name=name
        self.age=age
        self.gender=gender
        self.Dob=DOB




class student(person):
    def __init__(self, name, age, gender, DOB,Roll,std,school):
        super().__init__(name, age, gender, DOB)    
        self.Roll_No=Roll
        self.std=std
        self.school=school

    def student_Data(self):
            print("Roll No:", self.Roll_No)
            print("Standard:", self.std)
            print("School:", self.school)
            print("Name:", self.name)
            print("Age:", self.age)
            print("Gender:", self.gender)
            print("DOB:", self.Dob)
        


C1=student("Ali",17,"Male",3/11/2009,10,11,"MHS")            
C1.student_Data()




