import datetime,bday_messages

today= datetime.date.today()
next_birthday = datetime.date(2025,5,26)

days_awy = next_birthday - today

if today == next_birthday:
    print(bday_messages.rand_msg)
else:
    print(f'my next birthday is {days_awy} days away!')