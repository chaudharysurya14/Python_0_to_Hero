from  classes_objects_demo import Student
class Hpcsa_student(Student):

    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course,rcv_alternate_skill_set):
        # call to # initialiser of the parent class Student
        super().__init__(rcv_name,rcv_rollno,rcv_pocket_money,rcv_course)
        
        # instance variable
        self.__alternate_skill_set = rcv_alternate_skill_set
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course},{rcv_alternate_skill_set}")

    # instance method (getter)
    def get_alternate_skill_set(self):
         return self.__alternate_skill_set

    # instance method (setter)
    def set_a_alternate_skill_set(self,rcv_new_skill):
         self.__alternate_skill_set.append(rcv_new_skill)

    # instance method (setter)
    def set_many_alternate_skill_set(self,rcv_new_skill):
         self.__alternate_skill_set.extend(rcv_new_skill)


# main method 
# create a Student object referenced by bhawna
bhawna = Hpcsa_student("Bhawna",1,100,'Python',["C","C++","Python"])

# accessing things that the parent class provides and not defined in Hpcsa_student class
print(bhawna.student_enrolled_coursename)
bhawna.unenroll()
print(bhawna.student_enrolled_coursename)

# add a skill to the object referenced by bhawna
#print(bhawna.__alternate_skill_set)
print(bhawna.get_alternate_skill_set())
bhawna.set_a_alternate_skill_set("Perl")
print(bhawna.get_alternate_skill_set())

# add many skills to the object referenced by bhawna
print(bhawna.get_alternate_skill_set())
bhawna.set_many_alternate_skill_set(["Docker","Git"])
print(bhawna.get_alternate_skill_set())


