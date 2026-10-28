# name=input("Enter your name")
# age = int(input("Enter your age: "))
# print("\nWelcome to your AIML journey,", name)
# print("Next year, you will be", age + 1)


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# goal = input("What is your AIML goal? ")
# print("\n--- Your Profile ---")
# print("Name:", name)
# print("Age:", age)
# print("Next year you will be:", age + 1)
# print("AIML goal:", goal)
# print("Profile created successfully!")


# a = 10
# b = 3
# print(a + b)   # Addition
# print(a - b)   # Subtraction
# print(a * b)   # Multiplication
# print(a / b)   # Division
# print(a // b)  # Floor division
# print(a % b)   # Remainder
# print(a ** b)  # Power


# age = 20
# print(age > 18)
# print(age < 18)
# print(age == 20)
# print(age != 20)
# print(age >= 20)
# print(age <= 18)


# num=int(input("Enter the number :"))
# if num%2 == 0 :
#     print("Even number")
# else:
#     print("Odd number")


# # List
# subjects = ["Python", "Maths", "Statistics"]
# subjects.append("Machine Learning")
# print("Subjects:", subjects)

# # Tuple
# student_info = ("Archi", 2)
# print("Student:", student_info)

# # Dictionary
# student = {"name": "Archi", "cgpa": 8.4}
# student["goal"] = "AI/ML Engineer"
# print("Profile:", student)

# # Set
# skills = {"Python", "SQL", "Python", "Git"}
# print("Unique skills:", skills)


def calculate_average(marks):
    return sum(marks) / len(marks)
def find_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
marks = []
for i in range(5):
    score = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)
average = calculate_average(marks)
result = find_result(average)
print("\n--- Student Report ---")
print("Marks:", marks)
print("Average:", round(average, 2))
print("Result:", result)