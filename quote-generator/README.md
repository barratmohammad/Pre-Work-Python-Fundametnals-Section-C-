# Quote Generator

A tiny command-line program that prints a random inspirational quote each time
it runs. Built with only the Python standard library — no third-party packages.

## Requirements

- Python 3.8 or newer

## Setup

Clone or download the project, then from inside the `quote-generator` folder:

```bash
# 1. Create a virtual environment named "venv"
python3 -m venv venv

# 2. Activate it
#    macOS / Linux:
source venv/bin/activate
#    Windows (PowerShell):
venv\Scripts\Activate.ps1
#    Windows (Command Prompt):
venv\Scripts\activate.bat

# 3. Install dependencies (none here, but this is the standard step)
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Example output:

```
"Quality is not an act, it is a habit." — Aristotle
```

Run it again for a different quote.

## Leaving the environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## Project structure

```
quote-generator/
├── main.py            # the program
├── requirements.txt   # dependency list (empty: stdlib only)
├── .gitignore         # files Git should ignore (e.g. venv/)
└── README.md          # this file
```
