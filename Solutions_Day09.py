class Employee:
  # class variable 
  cls_department_name= "CDAC"
  
  def __init__(self,rcv_empid,rcv_emp_salary,rcv_mgr_id):
    # instance variables 
    self.empid= rcv_empid
    self.emp_salary= rcv_emp_salary
    self.mgr_id= rcv_mgr_id
    print(f"{self} was created successfully with values {rcv_empid},{rcv_emp_salary},{rcv_mgr_id}")

  # instance method
  def get_emp_salary(self):
      return self.emp_salary
  
  # instance method
  def set_emp_salary(self,rcv_salary):
      self.emp_salary = rcv_salary

  # class method 
  @classmethod
  def get_department_name(cls):
      return cls.cls_department_name
  
  # static method
  @staticmethod
  def field_expertice():
      print("Some expertise printed here")
  
def main():

    # 1) create an object employee(100,1000,1)  
    my_first_emp_obj = Employee(100,1000,1)
    
    #2) do the following for the created object
    #direct access using .notation
    print(f"Employee id for the object is {my_first_emp_obj.empid}")
    print(f"Salary for the object is {my_first_emp_obj.emp_salary}")
    print(f"Manager id for the object is {my_first_emp_obj.mgr_id}")
    
    #3) print the department name 
    Employee.get_department_name()
    my_first_emp_obj.get_department_name()
    
    #4) display the expertise for the employees
    Employee.field_expertice()
    my_first_emp_obj.field_expertice()

main()    