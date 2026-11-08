#================== Problem 1 =======================
'''
1. Shopping Discount Calculator

Requirements:
- Ask for customer name.
- Ask whether the customer has a membership.
- Take the shopping amount.
- Apply a 10% discount if the customer has membership and spends at least 1,000.
- Display the final price.
'''
print("==================Membership Discount================")
customer_name=input("Enter Name: ")
membership_status=input("Have Membership?(Yes/No)").lower()
total_shopping=int(input("Enter total shopping amount:$"))
member=True if membership_status=="yes" else False
discount=total_shopping*(10/100) if member and total_shopping>=1000 else 0
final_price= total_shopping - discount
#=====================Output==========================
print("\n Customer name:",customer_name)
print("Membership Status:",member)
print("Total shopping:",total_shopping)
print("Discount:",discount)
print("Final Price:",final_price)

#================== Problem 2 =======================
'''
2. Simple Bill Splitter

Requirements:
- Take the total bill.
- Take the number of people.
- Take the tip percentage.
- Calculate the tip amount.
- Calculate the final bill.
- Divide the bill equally among everyone
'''
print("=============Simple Bill Splitter==================")
total_bill=float(input("Total biil amount:$"))
number_of_people=int(input("Number of people sharing bill: "))
tips=int(input("Enter the tips amount(%):"))
tips_cash=total_bill*(tips/100)
total_bill=total_bill + tips_cash
shared_bill=total_bill / number_of_people
#=====================Output==========================
print(f"\nTotal biil amount:${total_bill}")
print(f"Number of people shared bill:{number_of_people}")
print(f"Tip({tips}%):",tips_cash)
print("Final Bill:$",total_bill)
print("Each person Pay:$",shared_bill)

#================== Problem 3 =======================
'''
3. Temperature Converter
Requirements:
- Convert Celsius to Fahrenheit.
- Convert Fahrenheit to Celsius.
- Accept decimal temperatures.
'''

print("=================Temperture Calculator\n====================")
celsius=float(input("Enter Celsius to convert Fahrenheit:"))
celsius_to_fahrenheit=(celsius*(9/5))+32
fahrenheit=float(input("Enter Fahrenheit to convert Celsius:"))
fahrenheit_to_celsius=(fahrenheit-32)*(5/9)
print(f"Fahrenheit:{celsius_to_fahrenheit:.2f}°F")
print(f"Celsius:{fahrenheit_to_celsius:.2f}°C")

#================== Problem 4 =======================
'''
4. Subject Search — Membership Operator

Requirements:
- Create a list of subjects.
- Ask the user to enter a subject.
- Check whether the subject exists using in.
- Display True or False.
'''
subjects = ["Python", "Mathematics", "English", "Physics"]
search=input("Enter your interested subject:").capitalize()
print("Subject exist:",search in subjects)
print("Subject doesn't exist:",search not in subjects)

#================== Problem 5 =======================
'''
5. Scholarship Eligibility Calculator

Requirements:
- Take student age.
- Take student marks.
- Take attendance percentage.
- A student qualifies if:
  - Age is at least 18.
  - Marks are at least 80.
  - Attendance is at least 75%.
- Display scholarship eligibility using a conditional expression.
'''
print("======================Scholarship check=======================")
student_name=input("Enter Name:")
student_age=int(input("Enter age:"))
student_marks=float(input("Enter marks out of 100:"))
student_attendance=float(input("Enter attendance in percentange:"))
scholarship_status="Eligible" if student_age>=18 and student_marks>=80 and student_attendance>=75 else "Not Eligible"
print("Name:",student_name)
print("Age:",student_age)
print("Marks",student_marks)
print("Attendence:",student_attendance)
print("Scholarship:",scholarship_status)