class Student:
    """ This is doctstring for Student class """
    # class variable
    school_name = "CDAC"    
    
    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
        # instance variable
        self.__student_name = rcv_name      # private instance variable 
        self._student_rollno = rcv_rollno   # protected instance variable
        self.student_pocket_money = rcv_pocket_money # public instance variable 
        self.student_enrolled_coursename = rcv_course # public instance variable 
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

    # instance method
    def get_enrolled_course(self):
        return self.student_enrolled_coursename

    # instance method
    def get_student_pocket_money(self):
        return self.student_pocket_money
    
    # instance method
    def enroll(self,rcv_course_name):
        self.student_enrolled_coursename = rcv_course_name

    # instance method
    def unenroll(self):
        self.student_enrolled_coursename = None

    # class method
    @classmethod
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname
    
    # static method
    @staticmethod
    def display_facilities_available():
        print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
       
    # Operator Overloading -- implemented this to support greater than operation for Student class 
    def __gt__(self,other_obj):
        return self._student_rollno > other_obj._student_rollno    
    
    # Operator Overloading -- implemented this to support Equal to operation for Student class 
    def __eq__(self,other_obj):
       return (self.__student_name == other_obj.__student_name  and 
               self._student_rollno == other_obj._student_rollno and
               self.student_pocket_money == other_obj.student_pocket_money and
               self.student_enrolled_coursename == other_obj.student_enrolled_coursename)

# main method which is outside the class 
def main():
    print("I am in main and I am not part of the class ")

    # create a Student object referenced by gaurav
    gaurav= Student("Gaurav",1,100,'Python')
    duplicate_gaurav= Student("Gaurav",1,100,'Scala')
    
    # accessed the private instance variable for gaurav referenced object outside the class 
    #print("Before setting the private variable : ", gaurav. nt_name)
    # set the private variable outside the class 
    #gaurav.__student_name = ""
    #print("After setting the private variable : ", gaurav.__student_name)
    #print("After setting the private variable : ", gaurav._Student__student_name)
    #print(dir(gaurav))
    
    # access the public instance variable for gaurav referenced object directly 
    print("Before setting the public variable : ",gaurav.student_pocket_money) 
    # set the public variable outside the class 
    gaurav.student_pocket_money = 9999999
    print("After setting the public variable : ", gaurav.student_pocket_money) 
    
    # access the protected instance variable for gaurav referenced object directly 
    print("Before setting the protected variable : ",gaurav._student_rollno) 
    # set the public variable outside the class 
    gaurav._student_rollno = 3333333
    print("After setting the protected variable : ", gaurav._student_rollno) 
    
    # invoke a instance method(getter) for gaurav referenced object to access an attribute of the class 
    print(gaurav.get_student_pocket_money())
    
    print("Before Unenroll call ", gaurav.get_enrolled_course())
    # invoke a instance method(setter) for gaurav referenced object to set an attribute of the class 
    gaurav.unenroll()
    print("After Unenroll call ", gaurav.get_enrolled_course())
    # invoke a instance method for gaurav referenced object 
    gaurav.enroll("Scala")
    print("After Enroll call ", gaurav.get_enrolled_course())

    pratik= Student("Pratik",2,200,'Java')
    print(pratik.get_student_pocket_money())
    
    print("Before Unenroll call ", pratik.get_enrolled_course())
    pratik.unenroll()
    print("After Unenroll call ", pratik.get_enrolled_course())
    pratik.enroll("C")
    print("After Enroll call ", pratik.student_enrolled_coursename)

    # trying to change the class variable using the Class reference 
    # print the class variable using each of the available references 
    print("School name at Class level was",Student.school_name)
    print("Gaurav School name was",gaurav.school_name)
    print("Pratik School name was",pratik.school_name)
    # invoke class method(setter) using Student class reference
    Student.change_schoolname("Sunbeam")

    # print the class variable 
    print("School name at Class level is",Student.school_name)
    print("Gaurav School name is",gaurav.school_name)
    print("Pratik School name is",pratik.school_name)

    # trying to change the class variable using the instance reference gaurav
    # print the class variable using each of the available references 
    print("School name at Class level was",Student.school_name)
    print("Gaurav School name was",gaurav.school_name)
    print("Pratik School name was",pratik.school_name)

    # invoke class method(setter) using gaurav instance variable reference
    gaurav.change_schoolname("CDAC")

    # trying to change the class variable using the instance reference gaurav's . notation
    # print the class variable 
    print("School name at Class level was",Student.school_name)
    print("Gaurav School name was",gaurav.school_name)
    print("Pratik School name was",pratik.school_name)
    # invoke class method using gaurav reference 
    
    #gaurav.change_schoolname("CDAC") # this will change the class variable 
    gaurav.school_name = "Sunbeam" # this will create a new instance variable for gaurav instance 

    # print the class variable 
    print("School name at Class level is",Student.school_name)
    print("Gaurav School name is",gaurav.school_name)
    print("Pratik School name is",pratik.school_name)    

    
    # invoke the static method 
    Student.display_facilities_available()
    gaurav.display_facilities_available()
    pratik.display_facilities_available()
    #display_facilities_available() # doesnot work 
    
    # Deleting Attributes __student_name
    #print(gaurav.__student_name)
    
    #AttributeError: 'Student' object has no attribute '__student_name'
    #del gaurav.__student_name 
    #print(gaurav.__student_name)
    #print(pratik.__student_name)
    
    # Deleting entire object gaurav
    #UnboundLocalError: local variable 'gaurav' referenced before assignment
    #del gaurav
    #print(gaurav.__student_name)
      
    # two references to the same object and deleting any one of the reference 
    gaurav_duplicate_reference = gaurav
    del gaurav_duplicate_reference
    print(gaurav._Student__student_name)

    #miscellnous functions for the class 
    # list all that the Student Class contains 
    print(dir(Student))
    print(Student.__doc__)
    
    # operator > is overloaded 
    if gaurav>pratik:
        print("Greater")
    else:
        print("Lesser")
                
    # operator == is overloaded
    if gaurav==duplicate_gaurav:
        print("equal")
    else:
        print("not equal")
        
# invoke the main function 
if __name__ == "__main__":
    main()
