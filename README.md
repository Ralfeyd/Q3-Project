# Q3-Project
Luke Duran 

Quiz Bowl instructions
Admin password: Password1

This is a Python-based Quiz Bowl application with a graphical user interface (GUI) and SQLite database. It includes two main modes:
**Administrator Interface** (password-protected): Add, edit, view, and delete quiz questions
**User Interface**: Take quizzes by course category, view score summary, and track answered questions live

QuizBowl/
├── main.py                    # Main entry point for the app
├── Admin_interface.py         # GUI and logic for admin features
├── User_interface.py          # GUI and logic for user quizzes
├── Question.py                # Question class definition
├── Database.py                # Code to initialize SQLite database
├── Quiz.db                    # SQLite database (auto-generated)
├── README.md                  # This file

### How to run
## 1. run the code in Main.py

    Administrator Mode

        Access 
        - From the home screen, click Admin
        - Enter the password (default: `Password1`)

        Features
        -Add Question Fill in question, answer options, and correct option
        - View Questions: Load and view all questions by course
        - Edit/Delete Questions: Scroll through the list of questions and:
            - Click Edit to update a question
            - Click Delete to remove it from the database

### Using the Scrollbar in Admin Mode
    If the list of questions exceeds the window size:
    - A vertical scrollbar will appear on the right
    - You can click and drag the scrollbar
    - Or use your mouse wheel / touchpad scrolling to scroll up and down

    This makes it easy to manage a large number of quiz questions.

### User Mode

    Access
    - From the home screen, click **Take Quiz**
    - Select a course from the dropdown and start

    Quiz Flow
        - All questions are shown at once
        - Select one answer per question
        - Track your progress with the "Answered: X / Total" counter
    - When ready, click **Submit Quiz** to:
    - View your final score
    - See how many were left unanswered
    - Click Return to Home to take another quiz

### Using the Scrollbar in User Mode
If the quiz has many questions:
- Use the scrollbar on the right to move up and down
- You won't see feedback until after submission

---

## Database

- Database file: `Quiz.db` (auto-generated)
- Contains 5 course tables:
  - ProgrammingLogicAndAnalyticalThinking
  - BusinessDatabaseManagement
  - DataDrivenDecisionMaking
  - BusinessApplicationsDevelopment
  - PrinciplesOfAccountingII

Each table includes:
- `id`, `question`, `option_a`, `option_b`, `option_c`, `option_d`, `correct_option`
Customization

You can update:
- Admin password in `Admin_interface.py`:

- Course names or table names in `Database.py`, `User_interface.py`, and `Admin_interface.py` as needed