#begin
#Initialize an empty list or dictionary to store courses
#Ask the user how many courses they want to input
#Repeat the following for each course:
#Ask the user to input the course ID (e.g., "COS 2005")
# Ask the user to input the course name (e.g., "Python Programming")
# Store the course ID and course name pair in the list or dictionary
#Ask the user to input a subject (e.g., "COS")
#Search through the list/dictionary for courses that match the inputted subject
#For each course, check if the course ID starts with the inputted subject.
#Display all the courses that match the inputted subject
#For each matching course, print out the course ID and course name.
#End the program


#Ben Krehbiel
#3/21/2025
#course registry


courses = {}


num_courses = int(input("How many courses would you like to input? "))


for _ in range(num_courses):
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses[course_id] = course_name

subject = input("Enter the subject to search for: ")

print(f"\nCourses with subject '{subject}':")
for course_id, course_name in courses.items():
    if course_id.startswith(subject):
        print(f"{course_id}: {course_name}")
