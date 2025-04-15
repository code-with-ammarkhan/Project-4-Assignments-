import streamlit as st

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

    st.title("💪 Body Mass Index (BMI) Calculator")
    st.write("Enter your details below to calculate your BMI.")

    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
    with col2:
        height = st.number_input("Enter your height (meters):", min_value=0.1, step=0.01)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        if bmi:
            st.success(f"Your BMI is: {bmi}")

            if bmi < 18.5:
                st.warning("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.info("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Invalid input! Please check your height.")

if __name__ == "__main__":
    main()
