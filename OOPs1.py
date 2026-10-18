
#Create an Employee class with attributes such as emp_id, name, department, designation, salary, and city. 
#Create an object ofthe class and display the complete details of the employee. 
#Also, create methods to calculate annual salary and display employee information.

 

class Employee:
    cuntry="India"
    def __init__(self,emp_id,name,department,designation,salary,city):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.designation=designation
        self.salary=salary
        self.city=city

    def calculate_annual_salary(self):
            return self.salary * 12    


    def employee_information(self):
         print("Employee_id :", self.emp_id)
         print("Name        :",self.name)
         print("department  :",self.department)
         print("designation :",self.designation)
         print("salary      :",self.salary)
         print("city        :",self.city)
         print("cuntry      :",self.cuntry)

emp1 = Employee(101, "Ali", "IT","Python Developer", 45000, "Pune")

emp1.employee_information()    



































