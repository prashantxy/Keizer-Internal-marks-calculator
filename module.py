import streamlit as st

st.set_page_config(
    page_title="INTERNAL MARKS CALCULATOR BY KEIZER",
    page_icon=":tada:",
)

st.title("INTERNAL MARKS CALCULATOR BY KEIZER")


def theory_sub():
    MST_1 = st.number_input("Enter MST 1 marks (Max: 20)", min_value=0, max_value=20)
    res_1 = MST_1 / 2
    MST_2 = st.number_input("Enter MST 2 marks (Max: 20)", min_value=0, max_value=20)
    res_2 = MST_2 / 2
    attendance = st.number_input("Enter attendance marks (Max: 2)", min_value=0, max_value=2)
    assignment = st.number_input("Enter assignment marks (Max: 12)", min_value=0, max_value=12)
    case_study = st.number_input("Enter case study marks (Max: 16)", min_value=0, max_value=16)
    res_3 = case_study / 2

    total = res_1 + res_2 + res_3 + assignment + attendance

    if total > 40:
        st.error("Entered marks seem invalid. Please check and re-enter.")
        return None

    st.write("**INTERNAL MARKS:**", total)
    return total

def practical_sub():
    lab_mst = st.number_input("Enter lab mst marks (Max: 15)", min_value=0, max_value=15)
    assessments = st.number_input("Enter the Number of assessments (Max: 3)", min_value=1, max_value=3)
    sum_assessments = 0

    for i in range(assessments):
        assessment_marks = st.number_input(f"Enter assessment {i+1} marks (Max: 15)", min_value=0, max_value=15)
        if assessment_marks > 15:
            st.error("Assessment marks cannot exceed 15. Please re-enter.")
            return None
        sum_assessments += assessment_marks

    total = lab_mst + sum_assessments

    if total > 60:
        st.error("Entered marks seem invalid. Please check and re-enter.")
        return None

    st.write("**INTERNAL MARKS:**", total)
    return total


def hybrid_subject():
    lab_mst = st.number_input("Enter lab mst marks (Max: 15)", min_value=0, max_value=15)
    assessments = st.number_input("Enter the Number of assessments (Max: 3)", min_value=1, max_value=3)
    sum_assessments = 0

    for i in range(assessments):
        assessment_marks = st.number_input(f"Enter assessment {i+1} marks (Max: 15)", min_value=0, max_value=15)
        if assessment_marks > 15:
            st.error("Assessment marks cannot exceed 15. Please re-enter.")
            return None
        sum_assessments += assessment_marks

    MST_1 = st.number_input("Enter MST 1 marks (Max: 20)", min_value=0, max_value=20)
    res_1 = MST_1 / 4
    MST_2 = st.number_input("Enter MST 2 marks (Max: 20)", min_value=0, max_value=20)
    res_2 = MST_2 / 4
    attendance = st.number_input("Enter attendance marks (Max: 5)", min_value=0, max_value=5)
    assignment = st.number_input("Enter assignment marks (Max: 15)", min_value=0, max_value=10)
    case_study = st.number_input("Enter case study marks (Max: 16)", min_value=0, max_value=16)
    res_3 = case_study
    EST = st.number_input("Enter EST marks (Max: 40)", min_value=0, max_value=40)
    res_4 = EST / 2

    total = (sum_assessments / 2) + (lab_mst / 2) + res_2 + res_1 + ((assignment + res_3 + attendance) / 3) + res_4
    if total > 70:
        st.error("Entered marks seem invalid. Please check and re-enter.")
        return None  # Indicate invalid input

    st.write("**INTERNAL MARKS:**", total)
    return total


def aptitude_sub():
    MST_1 = st.number_input("Enter mst 1 marks (Max: 20)", min_value=0, max_value=20)
    res_1 = MST_1 / 2
    MST_2 = st.number_input("Enter mst 2 marks (Max: 20)", min_value=0, max_value=20)
    res_2 = MST_2 / 2
    assignment = st.number_input("Enter the assignment marks (Max: 12)", min_value=0, max_value=12)
    res_4 = assignment / 2
    Quiz = st.number_input("Enter the Quiz Marks (Max: 6)", min_value=0, max_value=6)
    surprise_test = st.number_input("Enter the surprise test marks (Max: 12)", min_value=0, max_value=12)
    res_3 = surprise_test / 3
    attendance = st.number_input("Attendance marks (Max: 2)", min_value=0, max_value=2)
    total = attendance + res_1 + res_2 + res_3 + res_4 + Quiz

    if total > 40:
        st.error("Entered marks seem invalid. Please check and re-enter.")
        return None

    st.write("**INTERNAL MARKS:**", total)
    return total


def main():
    option = st.selectbox("Choose an option:", ["Theory", "Practical", "Hybrid", "Aptitude"])

    if option == "Theory":
        theory_sub()
    elif option == "Practical":
        practical_sub()
    elif option == "Hybrid":
        hybrid_subject()
    elif option == "Aptitude":
        aptitude_sub()
    else:
        st.error("Invalid option. Please select a valid subject type.")


if __name__ == "__main__":
    main()

