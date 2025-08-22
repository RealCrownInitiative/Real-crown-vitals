import streamlit as st
import random
from datetime import datetime

# 📖 Hardcoded Bible verses (sample of 366)
bible_verses = [
    "Genesis 1:1 — 'In the beginning God created the heavens and the earth.'",
    "Exodus 15:26 — 'I am the Lord who heals you.'",
    "Leviticus 19:18 — 'Love your neighbor as yourself.'",
    "Numbers 6:24 — 'The Lord bless you and keep you.'",
    "Deuteronomy 31:6 — 'Be strong and courageous. Do not be afraid.'",
    "Joshua 1:9 — 'Do not be discouraged, for the Lord your God will be with you wherever you go.'",
    "Psalm 23:1 — 'The Lord is my shepherd; I shall not want.'",
    "Psalm 34:18 — 'The Lord is close to the brokenhearted.'",
    "Psalm 91:1 — 'He who dwells in the shelter of the Most High will rest in the shadow of the Almighty.'",
    "Proverbs 3:5 — 'Trust in the Lord with all your heart.'",
    "Proverbs 17:22 — 'A cheerful heart is good medicine.'",
    "Isaiah 40:31 — 'Those who hope in the Lord will renew their strength.'",
    "Isaiah 41:10 — 'Do not fear, for I am with you.'",
    "Jeremiah 29:11 — 'For I know the plans I have for you,' declares the Lord.",
    "Jeremiah 30:17 — 'I will restore you to health and heal your wounds.'",
    "Lamentations 3:22 — 'His compassions never fail.'",
    "Ezekiel 36:26 — 'I will give you a new heart and put a new spirit in you.'",
    "Daniel 12:3 — 'Those who lead many to righteousness will shine like the stars.'",
    "Hosea 6:1 — 'He has torn us, but He will heal us.'",
    "Joel 2:25 — 'I will restore to you the years the locusts have eaten.'",
    "Amos 5:24 — 'Let justice roll on like a river.'",
    "Micah 6:8 — 'Act justly, love mercy, walk humbly with your God.'",
    "Nahum 1:7 — 'The Lord is good, a refuge in times of trouble.'",
    "Habakkuk 3:19 — 'The Sovereign Lord is my strength.'",
    "Zephaniah 3:17 — 'He will rejoice over you with singing.'",
    "Zechariah 4:6 — 'Not by might nor by power, but by My Spirit.'",
    "Malachi 4:2 — 'The sun of righteousness will rise with healing in its rays.'",
    "Matthew 5:14 — 'You are the light of the world.'",
    "Matthew 6:33 — 'Seek first the kingdom of God.'",
    "Matthew 11:28 — 'Come to Me, all who are weary.'",
    "Matthew 28:20 — 'I am with you always.'",
    "Mark 11:24 — 'Whatever you ask for in prayer, believe that you have received it.'",
    "Luke 1:37 — 'Nothing is impossible with God.'",
    "Luke 12:7 — 'Even the hairs of your head are all numbered.'",
    "John 3:16 — 'For God so loved the world...'",
    "John 8:12 — 'I am the light of the world.'",
    "John 14:27 — 'Peace I leave with you; My peace I give you.'",
    "Acts 2:21 — 'Everyone who calls on the name of the Lord will be saved.'",
    "Romans 8:28 — 'In all things God works for the good of those who love Him.'",
    "Romans 12:2 — 'Be transformed by the renewing of your mind.'",
    "1 Corinthians 13:13 — 'Faith, hope, and love. But the greatest of these is love.'",
    "2 Corinthians 5:7 — 'We live by faith, not by sight.'",
    "Galatians 6:9 — 'Do not grow weary in doing good.'",
    "Ephesians 2:10 — 'We are God’s handiwork.'",
    "Philippians 4:13 — 'I can do all things through Christ.'",
    "Colossians 3:23 — 'Work at it with all your heart.'",
    "1 Thessalonians 5:16 — 'Rejoice always.'",
    "2 Timothy 1:7 — 'God gave us a spirit of power, love, and self-discipline.'",
    "Hebrews 11:1 — 'Faith is being sure of what we hope for.'",
    "James 1:5 — 'If any of you lacks wisdom, ask God.'",
    "1 Peter 5:7 — 'Cast all your anxiety on Him.'",
    "Revelation 21:4 — 'He will wipe every tear from their eyes.'",
    # Add more verses here to reach 366 total
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
st.markdown("📞 Developer Contact: +256788739050")
st.markdown("---")

# 🔢 Inputs
name = st.text_input("Your Name:", placeholder="Enter your full name")
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

# 🧠 Initialize memory
if "reports" not in st.session_state:
    st.session_state["reports"] = []

# 📖 Verse of the Day (rotates daily)
verse_index = datetime.now().timetuple().tm_yday % len(bible_verses)
verse = bible_verses[verse_index]

# 🧾 Results
if st.button("▶️ Run Assessment"):
    results = []
    results.append(f"👤 Name: {name}")
    results.append(assess_bmi(weight, height, age_group))
    results.append(assess_blood_pressure(systolic, diastolic, age_group))
    results.append(assess_blood_sugar(sugar, sugar_unit, sugar_type, age_group))
    results.append(assess_heart_rate(pulse, age_group))
    results.append(assess_temperature(temp))
    results.append(assess_spo2(spo2))

    st.markdown("## 📖 Verse of the Day")
    st.markdown(f"> {verse}")

    st.markdown("## 🧾 Assessment Summary")
    for section in results:
        st.markdown(section)

    full_report = "\n".join(results)
    full_report += f"\n\n📖 Verse of the Day:\n{verse}"
    full_report += f"\n\n🕒 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    st.download_button("📥 Download Report (.txt)", full_report, file_name="realcrown_assessment.txt")

    if st.button("💾 Save This Assessment"):
        st.session_state["reports"].append(full_report)
        st.success("✅ Assessment saved. Ready for new input.")
        st.experimental_rerun()

# 📧 Optional Message Box
st.markdown("---")
st.markdown("### 💬 Optional Message to Real Crown Initiative")
message = st.text_area("Write your message or feedback here (optional):", placeholder="You can share your thoughts or request follow-up...")

if message:
    st.info("📧 To send this message, click below to open your email app.")
    email_link = f"mailto:realcrowninitiative@gmail.com?subject=Vital%20Signs%20Feedback&body={message.replace(' ', '%20')}"
    st.markdown(f"[📨 Send Email](<{email_link}>)", unsafe_allow_html=True)
