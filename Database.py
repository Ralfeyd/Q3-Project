#Luke Duran 04/13/25

import sqlite3

def initialize_database():
    conn = sqlite3.connect('Quiz.db')
    c = conn.cursor()

    course_tables = [
        "ProgrammingLogicAndAnalyticalThinking",
        "BusinessDatabaseManagement",
        "DataDrivenDecisionMaking",
        "BusinessApplicationsDevelopment",
        "PrinciplesOfAccountingII"
    ]

    for table in course_tables:
        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_option TEXT NOT NULL CHECK(correct_option IN ('A', 'B', 'C', 'D'))
            )
        ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
