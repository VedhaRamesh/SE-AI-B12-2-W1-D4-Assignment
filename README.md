# Student Grade System

A Streamlit app for adding students and marks, viewing each student's letter grade, and checking class statistics.

The assignment app is in `grade_app.py` and uses Streamlit only. `firstapi.py` is retained as a separate FastAPI example; it is not used by the grade system.

## Set up and run

From this folder, create and activate a virtual environment, then install Streamlit:

```zsh
python3 -m venv venv
source venv/bin/activate
pip install streamlit
streamlit run grade_app.py
```

Open the local URL printed by Streamlit, usually <http://localhost:8501>. Stop the app with **Ctrl+C** and leave the environment with `deactivate`.

## Grade scale

| Mark | Grade |
| --- | --- |
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| 0-59 | E |

The app requires a student name and a numeric mark from 0 to 100. It displays an error and does not add the student for blank, non-numeric, or out-of-range values. Student entries are kept in Streamlit session state across reruns; the class average, highest mark, and lowest mark update as students are added.

## Submission

The roster screenshot is saved at [`screenshots/class-roster.png`](screenshots/class-roster.png). Include it and `grade_app.py` in the GitHub submission.