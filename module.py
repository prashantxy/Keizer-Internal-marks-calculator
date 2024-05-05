import streamlit as st

st.set_page_config(
    page_title="INTERNAL MARKS CALCULATOR BY KEIZER",
    page_icon=":tada:",
)

st.title("INTERNAL MARKS CALCULATOR BY KEIZER")
st.sidebar.success("Select a page above")

def theory_sub():
    MST_1 = float(input("Enter MST 1 marks "))
    res_1 = MST_1 / 2
    MST_2 = float(input("Enter MST 2 marks "))
    res_2 = MST_2 / 2
    attendance = int(input("Enter attendance marks "))
    assignment = float(input("Enter assignment marks "))
    case_study = float(input("Enter case_study marks "))
    res_3 = case_study / 2
    
    total = res_1 + res_2 + res_3 + assignment + attendance
    
    if total > 40:
        print("Marks toh sahi se daal lo ")
        return -1
    else:
        print("INTERNAL MARKS: ")
        return total

def practical_sub():
    lab_mst = float(input("Enter the lab mst marks "))
    assesment = int(input("Enter the Number of assesment "))
    if assesment > 3:
        print("Bhai kya chahte ho?, 3 hai assesment ")
        return
    
    sum = 0
    for i in range(assesment):
        assesment_marks = float(input("enter the assesment_marks "))
        if assesment_marks > 15:
            print("Tera kuchh nahi ho sakta, 15 hai upperlimit ")
            break
        sum += assesment_marks
    
    total = lab_mst + sum
    if total > 60:
        print("bhai marks toh sahi se daal le ")
        return -1
    else:
        print("INTERNAL MARKS: ")
        return total

def hybrid_subject():
    lab_mst = float(input("Enter the lab mst marks "))
    assesment = int(input("Enter the Number of assesment "))
    if assesment > 3:
        print("Bhai kya chahte ho?, 3 hai assesment ")
        return
    
    sum = 0
    for i in range(assesment):
        assesment_marks = float(input("enter the assesment_marks "))
        if assesment_marks > 15:
            print("bhai 15 hai upperlimit ")
            break
        sum += assesment_marks
    
    MST_1 = float(input("Enter MST 1 marks "))
    res_1 = MST_1 / 4
    MST_2 = float(input("Enter MST 2 marks "))
    res_2 = MST_2 / 4
    attendance = float(input("Enter attendance marks "))
    assignment = float(input("Enter assignment marks "))
    case_study = float(input("Enter case_study marks "))
    res_3 = case_study
    EST = float(input("Enter EST marks: "))
    res_4 = EST / 2
    
    total = (sum / 2) + (lab_mst / 2) + res_2 + res_1 + ((assignment + res_3 + attendance) / 3) + res_4
    if total > 70:
        print("bhai marks toh sahi se daal le ")
    return total

def aptitude_sub():
    MST_1 = float(input("Enter mst 1 marks: "))
    res_1 = MST_1 / 2
    MST_2 = float(input("Enter mst 2 marks: "))
    res_2 = MST_2 / 2
    assignment = float(input("Enter the assignment marks "))
    res_4 = assignment / 2
    Quiz = float(input("Enter the Quiz Marks "))
    surprize_test = float(input("Enter the surprise test marks "))
    res_3 = surprize_test / 3
    attendance = float(input("Attendance marks "))
    total = attendance + res_1 + res_2 + res_3 + res_4 + Quiz
    
    return total

def main():
    print("Online Internal Marks Calculator by KEIZER")
    print("Choose an option:")
    print("A. theory_subject marks")
    print("B. practical_subject marks")
    print("C. Hybrid Subject marks")
    print("D. Aptitude Subject marks")
    option = input("Your choice: ").lower()
    
    if option == 'a':
        print(theory_sub())
    elif option == 'b':
        print(practical_sub())
    elif option == 'c':
        print(hybrid_subject())
    elif option == 'd':
        print(aptitude_sub())
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()


