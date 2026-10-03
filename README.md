# Salary Prediction App

An end-to-end Machine Learning project that predicts an employee's salary based on their years of experience, built with scikit-learn and deployed as an interactive Streamlit web application.

## 📌 Project Description

This project demonstrates a complete ML workflow: loading and exploring a dataset, training a regression model, saving the trained model, and serving predictions through a web app. The user enters their years of experience, and the app returns a predicted salary instantly.

## 📊 Dataset

- **Source:** Salary Dataset (Years of Experience vs Salary)
- **Features:** `YearsExperience`
- **Target:** `Salary`

## 🤖 Model

- **Algorithm:** Linear Regression (scikit-learn)
- **Train/test split:** 80/20

### Evaluation Metrics

| Metric | Value |
|--------|-------|
| MAE    | ~3164.48 |
| RMSE   | ~3489.50 |
| R² Score | ~0.9827 |

## 🗂️ Project Structure

```
ML_Project/
│
├── data/
│   └── salary_data.csv
│
├── model/
│   └── model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Running Locally

1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**. [Add your deployed app link here]

## 🛠️ Built With

- Python
- pandas, scikit-learn, joblib
- Streamlit
