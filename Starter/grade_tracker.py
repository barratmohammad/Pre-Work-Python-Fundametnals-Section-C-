# grade_tracker.py — reads student grades from a CSV, generates a class report,
# and writes a formatted summary to grade_report.txt

import csv


def load_students(filepath):
    """Read the CSV file and return a list of student dictionaries."""
    try:
        with open(filepath, newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: could not find '{filepath}'. Check that the file exists.")
        return []


def calculate_average(grades):
    """Return the average of valid grades rounded to 1 decimal, or None."""
    valid_grades = []
    for grade in grades:
        if grade != "":          # skip missing values BEFORE converting
            valid_grades.append(float(grade))

    if not valid_grades:         # all grades were missing
        return None

    return round(sum(valid_grades) / len(valid_grades), 1)


def get_letter_grade(average):
    """Convert a numeric average to a letter grade, or 'N/A' if None."""
    if average is None:
        return "N/A"
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_report(students):
    """Build and return the summary report dictionary."""
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    student_results = []

    for student in students:
        name = student["student_name"]
        grades = [value for key, value in student.items() if key != "student_name"]

        average = calculate_average(grades)
        letter = get_letter_grade(average)
        grade_distribution[letter] += 1

        student_results.append({
            "name": name,
            "average": average,
            "letter_grade": letter,
        })

    # Class stats use only students who have a real average
    averages = [s["average"] for s in student_results if s["average"] is not None]

    return {
        "total_students": len(students),
        "class_average": round(sum(averages) / len(averages), 1) if averages else None,
        "highest_average": max(averages) if averages else None,
        "lowest_average": min(averages) if averages else None,
        "grade_distribution": grade_distribution,
        "student_results": student_results,
    }


def write_report(report, filepath):
    """Write the formatted report to a text file."""
    with open(filepath, "w") as file:
        file.write("=" * 40 + "\n")
        file.write("        CLASS GRADE REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write("--- Summary ---\n")
        file.write(f"Total students:   {report['total_students']}\n")
        file.write(f"Class average:    {report['class_average']}\n")
        file.write(f"Highest average:  {report['highest_average']}\n")
        file.write(f"Lowest average:   {report['lowest_average']}\n\n")

        file.write("--- Grade Distribution ---\n")
        for letter in ["A", "B", "C", "D", "F", "N/A"]:
            file.write(f"  {letter}: {report['grade_distribution'][letter]}\n")
        file.write("\n")

        file.write("--- Individual Results ---\n")
        for student in report["student_results"]:
            average = student["average"] if student["average"] is not None else "--"
            file.write(f"  {student['name']:<20} {average:>5}  ({student['letter_grade']})\n")


def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"  Loaded {len(students)} students.")

    if not students:
        return

    print("\nGenerating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for letter in ["A", "B", "C", "D", "F", "N/A"]:
        print(f"  {letter}: {report['grade_distribution'][letter]}")

    print("\nTop 5 students:")
    graded = [s for s in report["student_results"] if s["average"] is not None]
    top_five = sorted(graded, key=lambda s: s["average"], reverse=True)[:5]
    for student in top_five:
        print(f"  {student['name']:<20} {student['average']:>5}  ({student['letter_grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()
