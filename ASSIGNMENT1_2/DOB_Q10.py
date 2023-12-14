from datetime import date
'''today = date.today()
print(today)

print('Enter your DOB for calculate days!')
pday=int(input('Enter date in yyyy/mm/dd'))
pday.slice("-")
year=int(input('Year: '))
month=int(input('Month:'))
day=int(input('Day:'))
# day=
dob=(year,'-',month,'-',day)
'''

# ======================================================================================================
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

'''






"create a function that takes in date of birth from the user and returns age in days of the user"

def days_func():
    from datetime import date
    date_inp = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
    #print(date_inp)
    year, month, day = [int(item) for item in date_inp]
    today_date = date(year, month, day)
    #print(today_date)
    current_date = date.today() - today_date
    print(current_date)
    
days_func()'''