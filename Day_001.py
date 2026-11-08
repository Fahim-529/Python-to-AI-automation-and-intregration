#=========================Problem 1============================================
'''
### 1. Shopping Bill Calculator
Build a program that:

- Takes the customer's name.
- Takes the names and prices of three products.
- Calculates the total shopping cost.
- Applies a 10% discount.
- Displays the original price, discount amount, and final payable amount.
'''
print("==================Bill Store=============================\n")
name= input("Please Enter Your Name:")
product_1=input("Product 1: ")
product_1_price= float(input("Price:$"))
product_2=input("Product 2: ")
product_2_price= float(input("Price:$"))
product_3=input("Product 3: ")
product_3_price= float(input("Price:$"))
print("\n\n===============shopping Summary===========================")
print("Customer name:",name)
print(f"Products:{product_1},{product_2},{product_3}")
#print(f"Price:{product_1_price}+{product_2_price}+{product_3_price}=",product_1_price + product_2_price + product_3_price)
OrginalPrice=product_1_price + product_2_price + product_3_price
print("Orginal Price:$",OrginalPrice)
discount_price=OrginalPrice*(10/100)
print("Discount(10%):$",discount_price)
print("Final Ammount:$",OrginalPrice-discount_price)


#-------------------------------Problem 2---------------------------------------------
'''
2. Internet Bill Calculator
Build a program that:
- Takes the internet package price.
- Takes the extra data usage.
- Calculates the additional data charge.
- Calculates VAT.
- Displays the final internet bill.
'''
print("----------------------Monthly Internet Bill--------------------------------")
customer_name=input("Enter Name: ")
package_name=input("Package: ")
package_price=float(input("Package price:$"))
extra_GB_Use=float(input("Extra data used:"))
per_extra_GB_price=float(input("Extra package use price(per GB):$"))
extra_package_price=(extra_GB_Use*per_extra_GB_price)
package_subtotal=(package_price+extra_package_price)
Vat=(package_subtotal*(5/100))
final_bill=(package_subtotal+Vat)
#-------------input------------------------

#-------------output-----------------------
print("Monthly Internet Bill\n")
print(f"Customer: {customer_name}")
print(f"Package: {package_name}\n")

print("Description \t Amount")
print(f"Package price \t ${package_price}")
print(f"Extra data charge \t ${extra_package_price}")
print(f"Subtotal \t ${package_subtotal}")
print(f"Vat(5%) \t ${Vat}")
print(f"Final bill \t ${final_bill}")


#----------------------------Problem 3--------------------------------
'''
3. Student Marks Calculator

Build a program that:
- Takes a student's name.
- Takes marks for five subjects.
- Calculates total marks.
- Calculates average marks.
- Calculates percentage.
- Calculates bonus marks needed to reach 450.
'''
print("======================Student Result===============================\n")
student_name=input("Enter Name: ")
student_id=input("Enter Id:")
python_mark=int(input("Enter Python Marks:"))
mathematics_mark=int(input("Enter Mathematics Marks:"))
english_mark=int(input("Enter English Marks:"))
physics_mark=int(input("Enter Physics Marks:"))
programming_mark=int(input("Enter programming Marks:"))

total_marks=python_mark+mathematics_mark+english_mark+ physics_mark+programming_mark
avg_marks=total_marks/5
percentage=avg_marks
need_mark=450-total_marks

print("============Result Summary=====================")
print(f"Student Name: {student_name}")
print(f"Student Id: {student_id}\n")
print(f"Python: {python_mark}/ 100")
print(f"Mathematics: {mathematics_mark}/ 100")
print(f"English: {english_mark}/ 100")
print(f"Physics: {physics_mark}/ 100")
print(f"Programming: {programming_mark}/ 100\n")
print(f"Total Marks:{total_marks}/500")
print(f"Average Mark:{avg_marks}")
print(f"Percentage:{percentage}%")
print(f"{need_mark} marks needs to get 450 marks")




