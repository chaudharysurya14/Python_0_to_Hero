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
    
days_func()


