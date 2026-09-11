# Student Record & Games Application

A menu-driven Python console application developed for the CSC115 final project at the University of Miami in Fall 2025. It creates student records, calculates credit-weighted GPAs on a 4.0 scale, exports text transcripts, and includes three additional activities.

The original submitted Python source is preserved in this repository.

## Features

| Menu option | Feature | Behavior |
| --- | --- | --- |
| `1` | Student record | Collects student details and course entries, calculates GPA, and prints and saves a transcript. |
| `2` | Lottery number generator | Generates five unique, sorted numbers from 1–69 and a separate Power Number from 1–26. |
| `3` | Pig Latin | Moves the first character of each word to the end, adds `AY`, and displays the result in uppercase. |
| `4` | Rock Paper Scissors | Plays against a random computer choice, rejects invalid choices, and repeats tied rounds. |
| `9` | Exit | Ends the program. |

## How to run

Install Python 3. The program uses only the standard library; no additional packages are needed. It has been checked with Python 3.12.14.

1. Clone the repository:

   ```bash
   git clone https://github.com/sjr492/Student-Record-and-Games-Application.git
   cd Student-Record-and-Games-Application
   ```

2. Run the program:

   ```bash
   python Rivas_Sebastian_CSC115_Fall2025_Final_Project.py
   ```

   If your system uses `python3` or the Windows `py` launcher, substitute that command for `python`.

3. Follow the console prompts. Each activity returns to the main menu when finished.

## Student record example

Select option `1`, then enter the following values at the corresponding prompts:

```text
Enter student info (Full Name, Email, Major, Student ID): Alex Example, alex@example.com, Computer Science, 100001
How many courses (2-6)? 2

Course 1:
Enter course info (Course Name, Credit Hours, Letter Grade): CSC115, 3, A

Course 2:
Enter course info (Course Name, Credit Hours, Letter Grade): MTH161, 4, B+
```

The GPA is weighted by each course's credit hours:

```text
GPA = sum(grade points × credit hours) / sum(credit hours)
    = (4.0 × 3 + 3.3 × 4) / (3 + 4)
    = 3.60
```

The program displays the transcript and writes `Alex Example.txt` in the directory from which it was launched. See the [sample input](examples/student_record_input.txt) and the [transcript generated from that input](examples/sample_transcript.txt). The example uses fictional student details.

## Design and skills demonstrated

- **Object-oriented programming:** `Course` stores a course's name, credit hours, and letter grade. `Student` stores student details and a list of courses, calculates GPA, and generates transcripts.
- **Data structures:** A dictionary maps letter grades to grade points; lists hold courses, lottery numbers, and game choices.
- **Control flow:** Functions separate the four activities, while loops manage the menu, input retries, unique lottery draws, and tied game rounds.
- **Input handling:** Comma-separated fields are parsed and stripped; numeric conversions use `try`/`except`; grades and game choices are normalized for case.
- **File output and formatting:** Transcripts use formatted strings and a context manager to write a text file.

## Input behavior and limitations

This repository retains the final project's original behavior:

| Input or feature | Current behavior |
| --- | --- |
| Student details | Requires four comma-separated fields; does not validate email format, ID format, or empty fields. |
| Number of courses | Accepts integers from 2–6 and prompts again for invalid input. |
| Course details | Requires three comma-separated fields and integer credit hours. Invalid entries are skipped, so the transcript may contain fewer courses than requested. |
| Credit hours | Zero and negative integers are accepted; use positive credit hours for a meaningful GPA. |
| Letter grades | Accepts `A+`, `A`, `A-`, `B+`, `B`, `B-`, `C+`, `C`, `C-`, `D+`, and `D`, ignoring case. `D-` and `F` are not supported by the input workflow. |
| Transcript storage | Saves to `<Full Name>.txt`; a later transcript with the same filename overwrites it. Records are not reloaded between sessions, and filename or file-writing errors are not handled. |
| Pig Latin | Uses the assignment's simple first-character rule for every word; it does not apply special vowel, consonant-cluster, or punctuation rules. |

## Verification

The repository preparation checks exercised:

- The sample session, its `3.60` weighted GPA, and the saved transcript contents.
- Invalid menu input, malformed student details, course-count retries, lowercase grades, and GPA with no courses.
- Pig Latin output and lottery duplicate rejection, sorting, and boundary values.
- All six decisive Rock Paper Scissors matchups, invalid player input, and tie replay using controlled random choices.

These checks used the submitted source. The instructor's expected-output file was not included, so this is not a claim of comparison against that file or a complete test of every possible input.

## Files

| File | Purpose |
| --- | --- |
| `Rivas_Sebastian_CSC115_Fall2025_Final_Project.py` | Original final project source. |
| `examples/student_record_input.txt` | Reproducible student record session, including menu selection and exit. |
| `examples/sample_transcript.txt` | Transcript produced by the sample session. |
| `.gitignore` | Excludes Python caches, local environments, editor files, and transcripts generated in the repository root. |

## Academic context

- **Author:** [Sebastian Rivas](https://github.com/sjr492)
- **Course:** CSC115 – Python Programming for Everyone
- **Institution:** University of Miami
- **Term:** Fall 2025
- **Project:** Final project
