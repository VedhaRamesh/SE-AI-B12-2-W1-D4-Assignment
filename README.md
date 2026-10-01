# Student Grade System

A Streamlit app that converts a mark from 0 to 100 into a letter grade.

## Set up and run

From this folder, create and activate a virtual environment, then install Streamlit:

```zsh
python3 -m venv venv
source venv/bin/activate
pip install streamlit
streamlit run grade_system.py
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

The app accepts a numeric mark, rejects values outside 0-100, and displays an error for non-numeric input. Leaving the field blank displays no result until a mark is entered.

## Submission

Capture the app in the browser with at least three different marks, include this `grade_system.py`, and upload the project to a GitHub repository.