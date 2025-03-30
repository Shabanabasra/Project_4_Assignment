import streamlit as st

# Function to calculate BMI
def calc_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Function to determine BMI category and health advice
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ You may need to gain some weight with a balanced diet."
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight", "✔ Great job! Maintain a healthy lifestyle with exercise and a nutritious diet. 😊"
    elif 25 <= bmi < 29.9:
        return "Overweight", "⚠️ Consider a healthier diet and regular exercise to maintain a balanced weight."
    else:
        return "Obese", "⚠️ A healthy lifestyle is crucial! Focus on a proper diet and physical activity."

# Streamlit UI Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="📏", layout="centered")

# App Title and Description
st.title("🌟 BMI Calculator 🌟")
st.write("**Calculate Your Body Mass Index (BMI) and understand your health status. 💗🌌**")
st.markdown("---")

# Input Fields
st.subheader("📌 Enter Your Details")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, step=0.1, format="%.1f")

with col2:
    height = st.number_input("Height (m):", min_value=0.5, step=0.01, format="%.2f")

# Calculate Button
if st.button("📊 Calculate BMI", use_container_width=True):
    if weight > 0 and height > 0:
        bmi = calc_bmi(weight, height)
        category, advice = get_bmi_category(bmi)

        # Display Result
        st.success(f"🎯 **Your BMI:** {bmi} ({category})")
        st.info(advice)
    else:
        st.warning("🚨 Please enter valid weight and height values.")

st.markdown("---")

# Additional Health Tip
st.write("💡 **Tip:** Keep a balanced diet, stay active, and hydrate well for a healthy BMI! 🏃‍♂️🥗💧")