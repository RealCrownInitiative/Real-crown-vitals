import streamlit as st
import random
from datetime import datetime

def load_verses(file_path="bible_verses.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["Psalm 147:3 — 'He heals the brokenhearted and binds up their wounds.'"]
        
# 📖 Bible verses
bible_verses = [
    "3 John 1:2 — 'Beloved, I pray that you may prosper in all things and be in health, just as your soul prospers.'",
    "Jeremiah 30:17 — 'For I will restore health to you and heal you of your wounds,' says the Lord.",
    "Proverbs 17:22 — 'A cheerful heart is good medicine, but a crushed spirit dries up the bones.'",
    "Isaiah 40:31 — 'But those who hope in the Lord will renew their strength.'",
    "Psalm 147:3 — 'He heals the brokenhearted and binds up their wounds.'"
]
# 🧠 Assessment functions
def assess_bmi(weight, height, age):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:
        category = "Normal"
    elif bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return f"💪 BMI: {bmi:.1f} — {category}"

def assess_blood_pressure(systolic, diastolic, age):
    if systolic < 90 or diastolic < 60:
        status = "Low"
    elif systolic > 140 or diastolic > 90:
        status = "High"
    else:
        status = "Normal"
    return f"🩸 Blood Pressure: {systolic}/{diastolic} mmHg — {status}"

def assess_blood_sugar(sugar, unit, sugar_type, age):
    sugar_mmol = sugar / 18.0 if unit == "mg" else sugar
    if sugar_type == "fbs":
        status = "Normal" if 3.9 <= sugar_mmol <= 5.5 else "Abnormal"
    else:
        status = "Normal" if sugar_mmol <= 7.8 else "Abnormal"
    return f"🍬 Blood Sugar ({sugar_type.upper()}): {sugar:.1f} {unit} — {status}"

def assess_heart_rate(pulse, age):
    if age == "child":
        normal = (70, 110)
    elif age == "adolescent":
        normal = (60, 100)
    else:
        normal = (60, 100)
    status = "Normal" if normal[0] <= pulse <= normal[1] else "Abnormal"
    return f"❤️ Heart Rate: {pulse} bpm — {status}"

def assess_temperature(temp):
    status = "Normal" if 36.1 <= temp <= 37.2 else "Abnormal"
    return f"🌡️ Temperature: {temp:.1f} °C — {status}"

def assess_spo2(spo2):
    status = "Normal" if spo2 >= 95 else "Low"
    return f"🫁 Oxygen Saturation: {spo2}% — {status}"

# 🩺 Interface
st.set_page_config(page_title="RealCrown Vital Signs", layout="centered")
st.title("🩺 RealCrown Vital Signs Assessment")
st.markdown("Developed by **Sseguya Stephen Jonathan** | Powered by **Real Crown Initiative**")
st.markdown("---")

# 🔢 Inputs
age_group = st.selectbox("Age Group:", ["child", "adolescent", "adult"])
weight = st.number_input("Weight (kg):", min_value=10.0, max_value=200.0)
height = st.number_input("Height (m):", min_value=0.5, max_value=2.5)
systolic = st.number_input("Systolic BP (mmHg):", min_value=50, max_value=250)
diastolic = st.number_input("Diastolic BP (mmHg):", min_value=30, max_value=150)
sugar = st.number_input("Blood Sugar:", min_value=1.0, max_value=600.0)
sugar_unit = st.selectbox("Blood Sugar Unit:", ["mg", "mmol"])
sugar_type = st.selectbox("Blood Sugar Type:", ["fbs", "rbs"])
pulse = st.number_input("Heart Rate (bpm):", min_value=30, max_value=200)
temp = st.number_input("Body Temperature (°C):", min_value=30.0, max_value=45.0)
spo2 = st.number_input("Oxygen Saturation (%):", min_value=50, max_value=100)

# ▶️ Run Assessment
if st.button("Run Assessment"):
    results = []
    results.append(assess_bmi(weight, height, age_group))
    results.append(assess_blood_pressure(systolic, diastolic, age_group))
    results.append(assess_blood_sugar(sugar, sugar_unit, sugar_type, age_group))
    results.append(assess_heart_rate(pulse, age_group))
    results.append(assess_temperature(temp))
    results.append(assess_spo2(spo2))

import random

bible_verses = load_verses()
verse = random.choice(bible_verses)

st.markdown("## 📖 Verse of the Day")
st.markdown(f"> {verse}")


    st.markdown("## 🧾 Assessment Summary")
    for section in results:
        st.markdown(section)

    st.markdown("---")
    st.markdown("### 🙏 Reflection or Prayer")
    reflection = st.text_area("Write your thoughts here:", placeholder="Speak life, hope, and healing...")

    # 📥 Downloadable report
    full_report = "\n".join(results)
    if reflection:
        full_report += f"\n\n🙏 Reflection:\n{reflection}"
    full_report += f"\n\n🕒 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    st.download_button("📥 Download Report", full_report, file_name="realcrown_assessment.txt")





