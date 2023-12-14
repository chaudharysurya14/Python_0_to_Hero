from datetime import date
while(True):
    def age():
        today=date.today()
        print("Today's date::",today) 

        print("Enter today's date as asked::")
        a=int(input("Enter DATE as DD::"))
        b=int(input("Enter MONTH as MM::"))
        c=int(input("Enter YEAR as YYYY::"))
        
        print(input("Enter your name::"))
        print("Enter DOB date as asked::")
        p=int(input("Enter DATE as DD::"))
        q=int(input("Enter MONTH as MM::"))
        r=int(input("Enter YEAR as YYYY::"))

        x=abs(a-p)
        y=abs(b-q)
        z=abs(c-r)
        print("Your Age is::",z,"years",y,"month",x,"days")
        total_days=(z*365+y*30+x)
        print("Your age in days is::",total_days,"days")
    age()      
    back=("Enter quit to exit::") 
    if back=="quit":
        break   
       