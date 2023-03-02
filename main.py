score_point_map = {
    70: 5.0,
    60: 4.0,
    50: 3.0,
    45: 2.0,
    40: 1.0,
    0: 0.0
}

# Prompt the user to enter their courses and scores
courses = []
scores = []
credit_hours = []
while True:
    course = input("Enter a course (or 'done' to finish): ")
    if course.lower() == 'done':
        break
    while True:
        try:
            score = int(input('Enter Score for {}'.format(course)))
            break
        except ValueError:
            print('Invalid input, please type a number!')

    while True:
        try:
            credit_hour = float(input('Enter credit hour for {}'.format(course)))
            break
        except ValueError:
            print('Invalid input. Enter a floating pont value')

    courses.append(course)
    scores.append(score)
    credit_hours.append(credit_hour)


# Define a function to calculate the grade point value (GPV) for a given score
def calculate_gpv(score):
    for scores, grade_point in score_point_map.items():
        if score >= scores:
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


# make a main function
def main() -> None:
    cgpa = calculate_cgpa(scores, credit_hours)

    print("\nCourses and scores:")
    for course, score, credit_hour in zip(courses, scores, credit_hours):
        print("{}: {} ({} credits)".format(course, score, credit_hour))
    print("\nCGPA: {:.2f}".format(cgpa))


# correct d score_point_map
# consider the error in


if __name__ == '__main__':
    main()
