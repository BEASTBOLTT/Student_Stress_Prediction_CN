# 🎓 Student Stress Level Prediction System (Streamlit App)

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts the **stress level of students** based on their lifestyle and academic habits.

The system analyzes inputs such as sleep, study hours, screen time, physical activity, diet, and caffeine intake, and classifies stress into categories like **Low, Medium, or High**.

The application is built using **Streamlit**, making it easy to interact with and deploy.

---

## 🚀 Features

* 🔮 Predicts student stress level instantly
* 🧠 Uses trained Machine Learning model (Logistic Regression)
* 🎯 Accepts both numerical and categorical inputs
* 🎨 Clean and modern UI (Streamlit-based)
* ⚡ Fast and interactive interface
* 🌐 Ready for deployment on Streamlit Cloud

---

## 🧠 Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-learn
* Joblib

---

## ⚙️ Machine Learning Model

* Algorithm Used: Logistic Regression
* Data Preprocessing:

  * Missing values handled using mean/mode
  * Categorical features encoded manually
  * Numerical features scaled using StandardScaler
* Model Persistence:

  * Saved using Joblib (`.pkl` files)

---

## 📊 Input Features

### 🔢 Numerical Features:

* Age
* Daily Walk (km)
* Screen Time (hrs)
* Sleep (hrs)
* Study/Work (hrs)

### 🔤 Categorical Features:

* Gender
* Activity Level
* Diet Quality
* Caffeine Intake

---

## 🧩 Project Structure

```
student-stress-prediction/
│── app.py                 # Streamlit app
│── train.py              # Model training script
│── stress_model.pkl      # Trained model
│── scaler.pkl            # Scaler for numerical data
│── label_encoder.pkl     # Encoder for output labels
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd student-stress-prediction
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
conda create -n stress_env python=3.10
conda activate stress_env
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

### 5️⃣ Open in Browser

```
http://localhost:8501
```

---

## 💡 How It Works

1. User enters lifestyle and academic data
2. Inputs are encoded and preprocessed
3. Numerical values are scaled
4. Model predicts stress level
5. Result is displayed instantly

---

## ⚠️ Notes

* Ensure all `.pkl` files are present in the root directory
* Use Python 3.10 for compatibility
* If version warnings appear, they can be safely ignored for demonstration
* The model expects all input features to be provided

---

## 🎯 Future Improvements

* 📊 Add data visualization (charts/graphs)
* 🌐 Deploy publicly with custom domain
* 🎨 Add animations and advanced UI
* 🔐 Add authentication system

---


## 📜 License

This project is for educational purposes only.
