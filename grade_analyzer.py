# grade-analyzer.py uses conditionals and loops to process student data.

# Grades and their corresponding letter grades

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Tally grades and count pass/fail in one pass
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
passing = 0
failing = 0

for score in scores:
    grade = letter_grade(score)
    grade_counts[grade] += 1
    if score >= 60:
        passing += 1
    else:
        failing += 1

total = len(scores)
average = sum(scores) / total
highest = max(scores)
lowest = min(scores)

print("=== Grade Analyzer ===")
print(f"Total scores: {total}")
print(f"Average score: {average: .1f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Passing: {passing} ({passing / total * 100:.1f}%)")
print(f"Failing: {failing} ({failing / total * 100:.1f}%")
print()
print("Grade distribution:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    print(f"{grade}: {grade_counts[grade]} students")

print()
print("---Add More Scores ---")
while True:
    entry = input("Enter a score (or 'done' to finish): ")
    if entry == "done":
        break
    new_score = int(entry)
    scores.append(new_score)
    avereage = sum(scores) / len(scores)
    print(f"Updated average: {average:.1f}")

print(f"Final average: {average:.1f}")