# Question 1: Write a program to create a file and do the following.
# Write 5 numbers into it
# Read the file
# Calculate and print the total sum

with open("file1.txt","w") as file:
    for i in range(5):
        i+1
        num=input("Enter number:")
        file.write(num+"\n")
total_sum=0    
with open("file1.txt","r") as file:
    for line in file:
        numbers = int(line.strip())
        total_sum += numbers
print(f"Total sum is: {total_sum}")
with open("file1.txt", "a") as file:
    file.write(f"Total Sum: {total_sum}\n")


# Question 2: Write a complete program that reads a CSV file containing student names and marks. 
# Displays each student’s grade
# Grades criteria:
# ≥ 80 → A
# ≥ 60 → B
# ≥ 50 → C
# < 50 → Fail

import csv
with open("grade.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Students name", "Marks","Grade"])
    for i in range(4):
        i+=1
        student_name=input("Student Name:")
        marks=int(input("Marks:"))
        if marks>=80:
            Grade="A"
            print(Grade)
        elif marks>=60:
            Grade="B"
            print(Grade)
        elif marks>=50:
            Grade="C"
            print(Grade)        
        else:
            Grade="FAIL"
            print(Grade)    
        writer.writerow([student_name, marks,Grade])

# Questions 3: Write a program that reads numbers from a text file.  
# Finds highest and lowest number
# Prints both values

with open("C:\\Users\\ayesh\\OneDrive\\Desktop\\Advance Python\\lab-12\\file1.txt","r") as file:
    numbers = [int(num) for num in file.read().split()]
    if numbers:
         highest = max(numbers)
         lowest = min(numbers)
         print("The highest number is:", highest)
         print("The lowest number is:", lowest)
    else:
        print("No Number")

# Question 4: Write a program to create a file 
# Write 5 numbers into it
# Count how many numbers are greater than 50

import csv
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

with open("number.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(numbers)
count = 0
for n in numbers:
    if n>50:
        count += 1
print(f"Total numbers greater than 50: {count}")


# Question 5: Write a program to: 
# 1. Ask user to enter 15 numbers.
# 2. Store them in a file.
# 3. Read the file and calculate:
# • Total sum
# • Average
# • Count of even numbers
# • Count of odd numbers
# • Largest number
# Store the outputs of the Question 5 in a separate file name “output.txt”.

with open("numbers.txt", "w") as file:
    for i in range(15):
        num = input(f"Enter number {i+1}: ")
        file.write(num+"\n")
numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))
total_sum = sum(numbers)
average = total_sum / len(numbers)
even_count = len([n for n in numbers if n % 2 == 0])
odd_count = len([n for n in numbers if n % 2 != 0])
largest = max(numbers)
with open("output.txt", "w") as out_file:
    out_file.write(f"Total Sum: {total_sum}\n")
    out_file.write(f"Average: {average}\n")
    out_file.write(f"Count of Even Numbers: {even_count}\n")
    out_file.write(f"Count of Odd Numbers: {odd_count}\n")
    out_file.write(f"Largest Number: {largest}\n")

# Question 6: Ask the user to enter data for 5 products:
# For each product ask:
# • Product Name
# • Quantity Sold
# • Price per Item
# Store the data in CSV format like this:
# Read the file again and for each product:
# • Calculate total sale amount
# (Total Sale = Quantity × Price)
# • Display:
# And you final CSV should show another column of total sales.

import csv
with open("product.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Quantity Sold", "Price per Item", "Total Sale"])
    for i in range(5):
        print(f"\nEntering data for Product {i+1}:")
        name = input("Product Name: ")
        qty = int(input("Quantity Sold: "))
        price = int(input("Price per Item: "))
        total = qty * price
        writer.writerow([name, qty, price, total])
    print(f"Total Sale for {name} is: {total}")



