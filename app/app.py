import streamlit as st
import requests

st.set_page_config(page_title="Personality Classifier", layout="centered")

st.title("🧠 Personality Prediction App")
st.write("Dự đoán bạn là **Introvert** hay **Extrovert** dựa trên hành vi xã hội.")

# 🎯 Input fields
with st.form("personality_form"):
    time_spent_alone = st.slider("⏰ Time Spent Alone", 0, 24, 5)
    social_events = st.slider("🎉 Social Event Attendance", 0, 10, 2)
    going_outside = st.slider("🚶 Going Outside", 0, 10, 3)
    friends_circle = st.slider("👥 Friends Circle Size", 0, 20, 6)
    post_frequency = st.slider("📱 Post Frequency", 0, 10, 2)

    stage_fear = st.selectbox("🎤 Stage Fear", ["Yes", "No"])
    drained_after_socializing = st.selectbox("😩 Drained After Socializing", ["Yes", "No"])

    submitted = st.form_submit_button("🔍 Dự đoán")

# 🚀 Send request if submitted
if submitted:
    input_data = {
        "Time_spent_Alone": time_spent_alone,
        "Social_event_attendance": social_events,
        "Going_outside": going_outside,
        "Friends_circle_size": friends_circle,
        "Post_frequency": post_frequency,
        "Stage_fear": stage_fear,
        "Drained_after_socializing": drained_after_socializing
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🎯 Bạn có xu hướng là: **{result['prediction']}**")
        else:
            st.error("❌ Lỗi khi gọi API. Kiểm tra FastAPI server.")
    except Exception as e:
        st.error(f"Không thể kết nối tới API: {e}")
