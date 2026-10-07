# import the streamlit library


# for feet bmi = weight / (((height/3.28))**2)

# bmi < 16: Extremely Underweight  --> Error
# 16 <= bmi < 18.5: Underweight  --> Warning
# 18.5 <= bmi < 25: Healthy  --> Success
# 25 <= bmi < 30: Overweight --> Info
# bmi >= 30: Extremely Overweight --> Error

import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator")
st.caption("Height in feet, weight in kilograms")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", min_value=0.1, value=70.0, step=0.5)
with col2:
    height = st.number_input(
        "Height (ft)",
        min_value=0.1,
        value=5.75,
        step=0.05,
        format="%.2f",
        help="Decimal feet, e.g. 5.75 for 5'9\"",
    )

height_m = height / 3.28
bmi = weight / (height_m ** 2)

st.divider()

st.metric("Your BMI", f"{bmi:.2f}")

# Visual gauge: maps a BMI range of 12-40 onto a 0-1 progress bar
gauge_min, gauge_max = 12, 40
position = min(1.0, max(0.0, (bmi - gauge_min) / (gauge_max - gauge_min)))
st.progress(position)

if bmi < 16:
    st.error("Extremely Underweight")
elif bmi < 18.5:
    st.warning("Underweight")
elif bmi < 25:
    st.success("Healthy")
elif bmi < 30:
    st.info("Overweight")
else:
    st.error("Extremely Overweight")

with st.expander("See BMI categories"):
    st.markdown(
        """
| BMI Range     | Category               |
|---------------|-------------------------|
| < 16          | Extremely Underweight   |
| 16 – 18.5     | Underweight             |
| 18.5 – 25     | Healthy                 |
| 25 – 30       | Overweight              |
| ≥ 30          | Extremely Overweight    |
"""
    )

st.caption("BMI is a general screening measure and doesn't account for muscle mass, bone density, or body composition.")