import streamlit as st


def grade_for_mark(mark: float) -> str:
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


st.title("Student Grade System")

mark_text = st.text_input("Enter your mark (0-100)", placeholder="For example, 85")

if mark_text.strip():
    try:
        mark = float(mark_text)
    except ValueError:
        st.error("Enter a valid number between 0 and 100.")
    else:
        if not 0 <= mark <= 100:
            st.error("Your mark must be between 0 and 100.")
        else:
            st.success(f"Mark: {mark:g} -> Grade: {grade_for_mark(mark)}")
