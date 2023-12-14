class My_house_members:
    
    hose_name = "CHAUDHARY"
    def __init__(self,rcv_name,rcv_age,rcv_pocket_money,rcv_work) -> None:
        self.member_name = rcv_name
        self.member_age = rcv_age
        self.member_pocket_money = rcv_pocket_money
        self.member_work = rcv_work
        print(f"{self} was created successfully with values {rcv_name},{rcv_age},{rcv_pocket_money},{rcv_work},")

    def get_member_work(self):
        return self.work_of_member
    
    def get_member_pocket_money(self):
        return self.pocket_money
    
    def work(self,rcv_work):
        self.member_work=rcv_work
        
    def workless(self):
        self.workless_member = None
        
    @classmethod
    def change_housename(cls,rcv_housename):
        cls.house_name = rcv_housename
        
    @staticmethod
    def display_facilities_available():
        print("Facilities are 1) Food\n2)Freedom\n3)TV\n")

def main():
    print('i am in main')    
        
    surya= My_house_members("Surya",1,100,'small_works')
    print(surya.member_name)
    print(surya.member_pocket_money)
    print("Before Enroll call ", surya.work_of_member())
    surya.enroll("Scala")
    print("After Enroll call ", surya.get_enrolled_course())


    sonu= My_house_members("sonu",2,200,'Java')
    print(sonu.student_name)
    print(sonu.get_student_pocket_money())
    print("Before Enroll call ", sonu.student_enrolled_coursename)
    sonu.enroll("C")
    print("After Enroll call ", sonu.student_enrolled_coursename)

    print("School name at Class level was",surya.school_name)
    print("Gaurav School name was",surya.school_name)
    print("sonu School name was",sonu.school_name)
    My_house_members.change_schoolname("Sunbeam")
    print("School name at Class level is",surya.school_name)
    print("Gaurav School name is",surya.school_name)
    print("sonu School name is",sonu.school_name)
    
    My_house_members.display_facilities_available()
    surya.display_facilities_available()
    sonu.display_facilities_available()
main()
