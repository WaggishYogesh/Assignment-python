      #Question 1 

print("1st program")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

avg = (x+y+z)/3

print("Average of numbers is: ",avg)      




        #Question 2

print("2nd program")

#Constants
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

#Taking input from the user
gross_income = float(input("\nEnter your gross income : "))
number_of_dependents = int(input("Enter number of dependents : "))

#Calculation of tax 
taxable_income = round(gross_income-standard_deduction-(dependent_deduction*number_of_dependents), 1)
tax = taxable_income*rate


print("Tax to be paid is $",tax,"\n")





              #Question 3

print("3rd program")

sid=int(input("Enter the sid = "))
name=input("Enter the name = ")
gender=input("Enter the gender F/M = ")
branch=input("Enter the branch name = ")
cgpa=float(input("Enter the cgpa = "))
student=[sid,name,gender,branch,cgpa]

print("Student: ",student)






              #Question 4

print("4th program")

M1= float(input("Enter the marks of 1st student= "))
M2= float(input("Enter the marks of 2nd student= "))
M3= float(input("Enter the marks of 3rd student= "))
M4= float(input("Enter the marks of 4th student= "))       
M5= float(input("Enter the marks of 5th student= "))

marks =[M1,M2,M3,M4,M5]
marks.sort()
print("Marks = ",marks)

      



              #Question 5
              
print("5th program")

color=['Red','Green','White','Black','Pink','Yellow']
COLOR1=[]
COLOR1.extend(color)
print("ORIGINAL LIST:",COLOR1)
COLOR1.pop(3)
print("List after removing 4th color: ",COLOR1)
color[3:5]=['Purple']
print("List after replacing black and pink by purple: ",color)