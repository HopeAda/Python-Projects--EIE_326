def gradeScore(grade):
    if grade == "A":
        return 5.0
    elif grade == "B":
        return 4.0
    elif grade == "C":
        return 3.0
    elif grade == "D":
        return 2.0
    elif grade == "F":
        return 0.0
    else:
        return "INVALID"

def main():
    print("This is a program to calculate the gpa of a student for 6 courses")
    
    courseInfo = []
    
    numberOfCourses = int(input("How many courses are you offering? "))
    
    for i in range(numberOfCourses):
        
        courseDetails = {}
        courseInfo.append(courseDetails)
        name = str(input(f"What is the name of course number {i+1}? "))
        courseDetails["courseName"] = name.upper()
        unit= int(input(f"What is the grade unit of course number {i+1}? "))
        courseDetails["courseUnit"] = unit
        grade = str(input(f"What is the grade of course Number {i+1}? "))
        courseDetails["courseGrade"] = grade.upper()
        
        
    
    sumOfUnit = 0
    unitSum = 0
    
    for course in courseInfo:
        if gradeScore(course["courseGrade"]) != "INVALID" and isinstance(course["courseUnit"], int) == True:
            gradePoint = course["courseUnit"] * gradeScore(course["courseGrade"])
            sumOfUnit = sumOfUnit + gradePoint
            unitSum = unitSum + course["courseUnit"]
        else:
            print("GPA cannot be calculated. Wrong input given. Try again")
            break
        
    if sumOfUnit != 0:
        gpa = sumOfUnit / unitSum
        print("These is the result for your courses: \n")
        for course in courseInfo:
            print(f"Course {courseInfo.index(course) + 1} :")
            for key, value in course.items():
                print(f"{key} : {value}")
            print()
            
        print(f"Your GPA for these {numberOfCourses} courses is {gpa:.2f}")
    
    
    
main()
