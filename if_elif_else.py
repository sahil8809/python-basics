## a human can vote or not

from datetime import datetime

dob = input("Enter your DOB (DD-MM-YYYY): ")

dob = datetime.strptime(dob, "%d-%m-%Y").date()
current_date = datetime.date.today()

# print("Your DOB is:", dob)
print(f"Your age = {current_date} - {dob}",current_date-dob)