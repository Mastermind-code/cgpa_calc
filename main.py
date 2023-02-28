
score_point_map = {
    (70, 100): 5.0,
    (60, 69): 4.0,
    (50, 59): 3.0,
    (45, 49): 2.0,
    (40, 44): 1.0,
    (0, 39): 0.0
}

# Prompt the user to enter their courses and scores
courses = []
scores = []
credit_hours = []
while True:
    course = input("Enter a course (or 'done' to finish): ")
    if course.lower() == 'done':
        break
    score = int(input("Enter the score for {}: ".format(course)))
    credit_hour = float(input("Enter the credit hour for {}: ".format(course)))
    courses.append(course)
    scores.append(score)
    credit_hours.append(credit_hour)

# Define a function to calculate the grade point value (GPV) for a given score
def calculate_gpv(score):
    for score_range, grade_point in score_point_map.items():
        if score in range(score_range[0], score_range[1] + 1):
            return grade_point
    return 0.0

# Define a function to calculate the CGPA for a given list of scores and credit hours
def calculate_cgpa(scores, credit_hours):
    total_quality_points = 0
    total_credit_hours = 0
    for score, credit_hour in zip(scores, credit_hours):
        gpv = calculate_gpv(score)
        quality_points = gpv * credit_hour
        total_quality_points += quality_points
        total_credit_hours += credit_hour
    if total_credit_hours == 0:
        return 0.0
    else:
        return total_quality_points / total_credit_hours


cgpa = calculate_cgpa(scores, credit_hours)

print("\nCourses and scores:")
for course, score, credit_hour in zip(courses, scores, credit_hours):
    print("{}: {} ({} credits)".format(course, score, credit_hour))
print("\nCGPA: {:.2f}".format(cgpa))
