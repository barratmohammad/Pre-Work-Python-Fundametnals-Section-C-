# Grade Tracker

A command-line Python application that reads student grade data from a CSV file,
calculates averages and letter grades, and writes a formatted class summary
report to a text file.

## Project Structure

```
grade_tracker/
├── data/
│   └── students.csv     # input: student names and grades
├── grade_tracker.py     # main program
├── requirements.txt     # empty — built-in modules only
└── README.md
```

## Requirements

- Python 3.8 or newer
- No external packages. The project uses only Python's built-in `csv` module,
  which is why `requirements.txt` is empty.

## Setup

1. Clone or download this project.
2. Make sure `data/students.csv` exists inside the project folder.

No virtual environment or `pip install` step is needed.

## How to Run

From the project root folder:

```
python3 grade_tracker.py
```

On Windows:

```
python grade_tracker.py
```

## What It Does

1. Loads student records from `data/students.csv`
2. Calculates each student's average, skipping any missing grades
3. Assigns letter grades (A: 90+, B: 80–89.9, C: 70–79.9, D: 60–69.9, F: below 60)
4. Prints a summary to the terminal: class average, highest/lowest average,
   grade distribution, and the top 5 students
5. Writes the full report, including individual results for every student,
   to `grade_report.txt`

## Error Handling

- **Missing file:** if `data/students.csv` is not found, the program prints a
  helpful message and exits cleanly instead of crashing.
- **Missing grades:** empty grade values are skipped; averages use only the
  valid grades.
- **No valid grades:** a student with no grades at all gets an average of
  `None` and a letter grade of `N/A`.
