import streamlit as st

def calculate_gpa(course_info):
    total_points = 0
    total_credits = 0

    for course in course_info:
        credits, grade = course['credits'], course['grade']
        grade_points = get_grade_points(grade)
        total_points += credits * grade_points
        total_credits += credits

    if total_credits == 0:
        return 0

    gpa = total_points / total_credits
    return gpa

def get_grade_points(grade):
    grade_points = {
        'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0
    }
    return grade_points.get(grade, 0)

def main():
    num_semesters = int(st.number_input("Enter the desired number of semesters:"))
    semester_gpas = []

    for semester in range(1, num_semesters + 1):
        st.header(f"Semester {semester}:")

        num_courses = int(st.number_input(f"Enter the number of courses for Semester {semester}:"))
        course_info = []

        for i in range(num_courses):
            course_name = st.text_input(f"Enter the name of course {i + 1}:", key=f"course_name_{semester}_{i}")
            credits = int(st.number_input(f"Enter the credit hours for course {i + 1}:", key=f"credits_{semester}_{i}"))
            grade = st.text_input(f"Enter the grade for course {i + 1} (e.g., A, B, C, etc.):", key=f"grade_{semester}_{i}")
            course_info.append({'name': course_name, 'credits': credits, 'grade': grade})

        gpa = calculate_gpa(course_info)
        st.success(f"Your GPA for Semester {semester} is: {gpa:.2f}")
        semester_gpas.append(gpa)
        st.write("\n")

    if semester_gpas:
        cgpa = sum(semester_gpas) / len(semester_gpas)
        st.success(f"Your Cumulative GPA (cGPA) for {num_semesters} semesters is: {cgpa:.2f}")
    else:
        st.warning("No semesters entered. Please enter at least one semester.")

if __name__ == "__main__":
    main()
