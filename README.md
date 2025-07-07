# 🧠 Personality Prediction Project (Introvert vs Extrovert)

This project uses a machine learning pipeline to predict whether a person is an **Introvert** or **Extrovert** based on behavioral traits such as social activity, time alone, and more.

The solution includes:

* ✅ Complete ML pipeline (EDA → preprocessing → model training)
* ✅ Deployment with **FastAPI**
* ✅ Web interface with **Streamlit**
* ✅ Saved model and pipeline for real-world inference

---

## 📁 Project Structure

```
personality-predictor/
├── app/                        # Deployment code
│   ├── app.py                 # Streamlit frontend
│   └── api.py                 # FastAPI backend
├── datasets/
│   └── personality_datasert.csv  # Input dataset
├── models/
│   ├── model.joblib           # Trained classifier
│   └── pipeline.joblib        # Preprocessing pipeline
├── notebooks/
│   └── training_pipeline.ipynb   # EDA + training notebook
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Start the FastAPI backend

```bash
cd app
uvicorn api:app --reload
```

Visit:

* `http://127.0.0.1:8000/docs` → Swagger UI to test predictions

---

### 3️⃣ Launch the Streamlit frontend

In a separate terminal tab:

```bash
cd app
streamlit run app.py
```

Visit:

* `http://localhost:8501` → Web UI for personality prediction

---

## 📊 Features Used

* `Time_spent_Alone`
* `Social_event_attendance`
* `Going_outside`
* `Friends_circle_size`
* `Post_frequency`
* `Stage_fear` (`Yes`/`No`)
* `Drained_after_socializing` (`Yes`/`No`)

---

## 🧠 Model Training

Training is done in:
📄 `notebooks/training_pipeline.ipynb`

Steps:

* Exploratory Data Analysis (EDA)
* Data validation (using `pandera`)
* Feature engineering & encoding
* Preprocessing pipeline
* Model training with `SGDClassifier`
* Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
* Saved model/pipeline to `models/`

---

## 📂 Dataset

* **File**: `datasets/personality_datasert.csv`
* **Source**: [Kaggle – Extrovert vs Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)

If the dataset is missing, download it and place it in the `datasets/` folder.
