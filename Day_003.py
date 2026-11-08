#========================================Project one=============================================================
'''
1. Student Management & Result Analyzer

This was your largest project so far.

Requirements:
- Ask how many students will be processed.
- Collect each student's name and age.
- Collect Python, Mathematics, and English marks.
- Validate student count.
- Skip empty student names.
- Validate marks between 0 and 100.
- Allow one retry for invalid marks; stop processing if the second attempt is invalid.
- Calculate total marks using +=.
- Calculate average and percentage.
- Assign grades:
Average	Grade
80–100	A+
70–79.99	A
60–69.99	B
50–59.99	C
40–49.99	D
Below 40	F

- Check scholarship eligibility using nested if/else:
  - Age at least 18.
  - Average at least 80.
  - Every subject mark at least 70.
- Create a subject list and search using in.
- Display each student's report.
'''

print("===========================Student Management & Result Analyzer============================")
invalid=False
student_numbers=int(input("Number of students:"))
while student_numbers <= 0 :
    student_numbers=int(input("Please Enter valid Number of students:"))

for x in range(student_numbers):
        total_number=0
        student_name=input(f"Student {x+1} name:")
        student_name=student_name.strip()
        if student_name=="":
                              continue
        
        student_age=int(input(f"Student {x+1} age:"))
       

        student_python_marks=float(input(f"Student {x+1} python marks:"))
        while student_python_marks>100 or student_python_marks<0:
                student_python_marks=float(input(f"Please enter valid Student {x+1} python marks:"))
                if student_python_marks>100 or student_python_marks<0:
                        invalid=True
                        print("Invaild mark!")
                        break
        total_number+=student_python_marks
        if invalid==True:
                break


        student_mathematics_marks=float(input(f"Student {x+1} Mathematics marks:"))
        while student_mathematics_marks>100 or student_mathematics_marks<0:
                        student_mathematics_marks=float(input(f" Please enter valid Student {x+1} mathematics marks:"))
                        if student_mathematics_marks>100 or student_mathematics_marks<0:
                                                invalid=True
                                                print("Invaild mark!")
                                                break
        total_number+=student_mathematics_marks
        if invalid==True:
                break


        student_english_marks=float(input(f"Student {x+1} English marks:"))
        while student_english_marks>100 or student_english_marks<0:
                        student_english_marks=float(input(f"Please enter valid Student {x+1} english marks:"))
                        if student_english_marks>100 or student_english_marks<0:
                                                invalid=True
                                                print("Invaild mark!")
                                                break
        total_number+=student_english_marks
        if invalid==True:
                 break

        subject_list=["Python","Mathematics","English"]
        subject_check=input("Enter favourite subject:").capitalize()
        if subject_check.strip() in subject_list:
                print("Exist!",subject_check)
        elif subject_check not in subject_list:
                print("Not exist!",subject_check)

        avg_marks = total_number/3
        percentage = (total_number / 300)*100
       
        if avg_marks >= 80:
                result = "A+"
        elif avg_marks >= 70:
                result = "A"
        elif avg_marks >= 60:
                result = "B"
        elif avg_marks >= 50:
                result = "C"
        elif avg_marks >= 40:
                result = "D"
        else:
                result="F"

        #Using tenrary opreator...
        # scholarship_status= "Eligible" if (student_age >= 18 and avg_marks >= 80) and min(student_english_marks,student_mathematics_marks,student_python_marks)>=70 else "Not Eligible"

        if student_age>=18 :
                if avg_marks>=80:
                        if min(student_python_marks,student_english_marks,student_mathematics_marks)>=70:
                                scholarship_status="Eligible"
                        else:
                                scholarship_status="Not Eligible"
                else:
                        scholarship_status="Not Eligible"
        else:
             scholarship_status="Not Eligible"

        print("\n\n=========================Students Details=================================")
        print("Student Name:",student_name)
        print("Student Age:",student_age)
        print("Student Python Marks:",student_python_marks)
        print("Student Mathematices Marks:",student_mathematics_marks)
        print("Student English Marks:",student_english_marks)
        print("Total Mark:",total_number)
        print(f"Average Mark:{avg_marks:.2f}")
        print(f"Percentange:{percentage:.2f}%")
        print("Result=",result)
        print("Scholarship Status:",scholarship_status)
        print("==========================================================")


#====================================Project 2===============================================
'''
2. Multiplication Tables Using Nested Loops

Requirements:
- Use an outer for loop for tables 1–5.
- Use an inner for loop for multipliers 1–10.
- Display all five multiplication tables.
'''
print("====================Multiplication Table=============================")
for x in range(6):
    print(f"\n{x}s Multiplication Table\n")
    for y in range(1,11):
        print(f"{x}x{y}=",x*y)