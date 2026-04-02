import streamlit as st
import numpy as np
import joblib

# Load model files
model = joblib.load("stress_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Page config
st.set_page_config(
    page_title="Student Stress Predictor", page_icon="🎓", layout="centered"
)

# Custom CSS (UI enhancement 🔥)
st.markdown(
    """
<style>
.main {
    background: linear-gradient(135deg, #667eea, #764ba2);
}
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
}
.title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
.result {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    '<div class="title">🎓 Student Stress Prediction</div>', unsafe_allow_html=True
)
st.write("Enter student details below:")

# Create layout (2 columns like modern UI)
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, step=1)
    walk = st.number_input("Daily Walk (km)", min_value=0, step=1)
    screen = st.number_input("Screen Time (hrs)", min_value=0, step=1)
    sleep = st.number_input("Sleep (hrs)", min_value=0, step=1)
    study = st.number_input("Study/Work (hrs)", min_value=0, step=1)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox("Activity Level", ["Low", "Medium", "High"])
    diet = st.selectbox("Diet Quality", ["Poor", "Average", "Good"])
    caffeine = st.selectbox("Caffeine Intake", ["Low", "Medium", "High"])

# Predict button
if st.button("Predict Stress"):

    try:
        # Encoding (EXACT SAME as your Flask app)
        gender_map = {"male": 1, "female": 0}
        activity_map = {"low": 1, "medium": 2, "high": 0}
        diet_map = {"poor": 2, "average": 0, "good": 1}
        caffeine_map = {"low": 1, "medium": 2, "high": 0}

        input_data = [
            age,
            walk,
            screen,
            sleep,
            study,
            gender_map[gender.lower()],
            activity_map[activity.lower()],
            diet_map[diet.lower()],
            caffeine_map[caffeine.lower()],
        ]

        input_array = np.array(input_data).reshape(1, -1)

        # Scaling (same as original)
        input_array[:, 0:5] = scaler.transform(input_array[:, 0:5])

        # Prediction (same model)
        prediction = model.predict(input_array)
        result = label_encoder.inverse_transform(prediction)[0]

        # Output styling
        st.markdown(
            f'<div class="result"> Stress Level: {result}</div>',
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")
