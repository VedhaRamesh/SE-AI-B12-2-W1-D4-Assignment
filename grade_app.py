import streamlit as st

st.set_page_config(
    page_title="Student Grade System",
    page_icon=":material/school:",
    layout="wide",
)


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


st.session_state.setdefault("students", [])
students = st.session_state.students

st.caption("CAIE COURSE PROGRAM / CLASS RECORDS")
st.title("Student Grade System", icon=":material/school:")

form_column, summary_column = st.columns([1, 1.8], gap="large")

with form_column:
    with st.form("add_student_form"):
        st.subheader("Add a student", icon=":material/person_add:")
        student_name = st.text_input("Student name", max_chars=80)
        mark_text = st.text_input(
            "Mark (0-100)", placeholder="Enter a number from 0 to 100"
        )
        submitted = st.form_submit_button(
            "Add student", type="primary", icon=":material/add:"
        )

    if submitted:
        clean_name = student_name.strip()
        if not clean_name:
            st.error("Enter a student name.")
        else:
            try:
                mark = float(mark_text)
            except ValueError:
                st.error("Enter a numeric mark between 0 and 100.")
            else:
                if not 0 <= mark <= 100:
                    st.error("Mark must be between 0 and 100.")
                else:
                    st.session_state.students.append(
                        {"name": clean_name, "mark": mark}
                    )
                    students = st.session_state.students
                    st.toast(f"Added {clean_name}.", icon=":material/check:")

with summary_column:
    st.subheader("Class at a glance", icon=":material/analytics:")
    if students:
        marks = [student["mark"] for student in students]
        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        with st.container(horizontal=True, gap="small"):
            st.metric("Class average", f"{average:.1f}", border=True)
            st.metric("Highest mark", f"{highest:g}", border=True)
            st.metric("Lowest mark", f"{lowest:g}", border=True)
        st.caption(f"{len(students)} students")
    else:
        with st.container(horizontal=True, gap="small"):
            st.metric("Class average", "--", border=True)
            st.metric("Highest mark", "--", border=True)
            st.metric("Lowest mark", "--", border=True)
        st.caption("Class statistics appear when students are added.")

    st.subheader("Grade scale", icon=":material/grade:")
    with st.container(horizontal=True, gap="small"):
        st.badge("A  90-100", color="green")
        st.badge("B  80-89", color="blue")
        st.badge("C  70-79", color="orange")
        st.badge("D  60-69", color="gray")
        st.badge("E  Below 60", color="red")

st.subheader("Student roster", icon=":material/groups:")
if students:
    rows = [
        {
            "Name": student["name"],
            "Mark": student["mark"],
            "Grade": grade_for_mark(student["mark"]),
        }
        for student in students
    ]
    st.dataframe(
        rows,
        column_config={
            "Mark": st.column_config.ProgressColumn(
                "Mark",
                format="%.1f",
                min_value=0,
                max_value=100,
                color="primary",
            )
        },
        hide_index=True,
    )
else:
    st.info("Add a student to see the class roster.", icon=":material/info:")