# This program collects exam points and exercise counts,
# converts them into total points, assigns grades,
# and prints overall statistics.

def user_input():
    # Collects user input until an empty line is entered
    # Each entry contains exam points and exercises completed
    results = []
    while True:
        entry = input("Exam points and exercises completed: ")
        if entry == "":
            break
        else:
            numbers = entry.split()
            pair = [int(numbers[0]), int(numbers[1])]
            results.append(pair)
    return results


def exercise_conversion(results: list):
    # Converts exercises into points (1 point per 10 exercises)
    # and adds them to exam points
    totals = []
    for i in results:
        total = i[0] + (i[1] // 10)
        totals.append(total)
    return totals


def grade_calculation(results, totals):
    # Assigns grades based on total points
    # Exam must be at least 10 points to pass
    grades = []
    for i in range(len(totals)):
        exam_points = results[i][0]
        total_points = totals[i]

        if exam_points < 10:
            grade = 0
        else:
            if 28 <= total_points <= 30:
                grade = 5
            elif 24 <= total_points <= 27:
                grade = 4
            elif 21 <= total_points <= 23:
                grade = 3
            elif 18 <= total_points <= 20:
                grade = 2
            elif 15 <= total_points <= 17:
                grade = 1
            else:
                grade = 0

        grades.append(grade)
    return grades


def points_average(totals: list):
    # Calculates the average of total points
    average = 0
    for i in totals:
        average += i
    averages = average / (len(totals))
    return averages


def pass_percentage(grades: list):
    # Calculates the percentage of students who passed (grade > 0)
    passers = 0
    count = 0
    fail = 0

    for i in grades:
        count += 1
        if i == 0:
            fail += 1

    passers = ((count - fail) / len(grades)) * 100
    return passers


def grade_distribution(grades: list):
    # Prints the number of each grade as stars
    print(f"5: {'*' * grades.count(5)}")
    print(f"4: {'*' * grades.count(4)}")
    print(f"3: {'*' * grades.count(3)}")
    print(f"2: {'*' * grades.count(2)}")
    print(f"1: {'*' * grades.count(1)}")
    print(f"0: {'*' * grades.count(0)}")


def main():
    # Main program flow
    results = user_input()
    totals = exercise_conversion(results)
    grades = grade_calculation(results, totals)
    averages = points_average(totals)
    passers = pass_percentage(grades)

    print("Statistics: ")
    print(f"Points average: {averages:.1f}")
    print(f"Pass percentage: {passers:.1f}")
    print("Grade distribution: ")
    grade_distribution(grades)


main()