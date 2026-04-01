# 🎓 Student Stress Level Prediction System

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts the **stress level of students** based on their lifestyle and academic factors.
The system uses a trained model to analyze inputs such as sleep, study hours, screen time, and diet, and outputs a stress category.

---

## 🚀 Features

* Predicts student stress level (Low / Medium / High)
* User-friendly web interface using Flask
* Handles both numerical and categorical inputs
* Real-time prediction
* Clean and modern UI

---

## 🧠 Technologies Used

* Python
* Flask
* NumPy
* Scikit-learn
* Joblib

---

## ⚙️ Machine Learning Model

* Algorithm Used: Random Forest / Logistic Regression (based on trained model)
* Data Preprocessing:

  * Numerical features scaled using StandardScaler
  * Categorical features encoded manually
* Model saved using Joblib (`.pkl` files)

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
│── app.py
│── stress_model.pkl
│── scaler.pkl
│── label_encoder.pkl
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd student-stress-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install flask numpy scikit-learn joblib
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 💡 How It Works

1. User enters lifestyle and academic data
2. Data is processed and encoded
3. Numerical values are scaled
4. Model predicts stress level
5. Result is displayed on the web page

---

## ⚠️ Notes

* Ensure all `.pkl` files are in the root directory
* If you see version warnings from scikit-learn, they can be ignored for demonstration purposes
* The model expects all input features to be provided

---

## 🎯 Future Improvements

* Add data visualization (charts/graphs)
* Deploy application online
* Improve UI with animations
* Add user authentication system

---

## 📜 License

This project is for educational purposes only.
