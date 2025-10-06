# Credit-Card-fraud-detection-dashboard
An interactive Streamlit dashboard for detecting fraudulent credit card transactions using an XGBoost model. Includes real-time fraud detection, sample data download, and visual insights.

# 💳 Credit Card Fraud Detection Dashboard

An interactive **Streamlit web application** for detecting fraudulent credit card transactions in real-time using a trained **XGBoost model**.

---

## 🚀 Features

- 🧠 Machine Learning model (XGBoost) trained on real-world credit card data  
- 📊 Real-time fraud detection from uploaded CSV datasets  
- 📥 Download sample data and prediction results  
- ⚡ Friendly error handling for non-transaction data  
- 📈 Professional dark Streamlit dashboard UI  
  

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/Credit-Card-fraud-detection-dashboard.git
cd fraud-detection-dashboard

### 2️⃣ Create a virtual environment

conda create -n fraudapp python=3.10
conda activate fraudapp

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ streamlit run fraud_dashboard.py




## 🧩 Model Information

The trained XGBoost model (fraud_xgb_model.json) achieves:

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99.96% |
| AUC       | 0.999  |
| Precision | 0.998  |
| Recall    | 0.997  |

##  🔒 5. `.gitignore`

Create a `.gitignore` file to prevent unnecessary uploads:
pycache/
*.pkl
*.log
*.csv
*.xlsx
.DS_Store
.env

## ✅ 6. Upload Steps


Open your terminal in the `Fraud_app` folder and run:

git init
git add .
git commit -m "Initial commit - Fraud Detection Dashboard"
git branch -M main
git remote add origin https://github.com/awesome-hubdata/Credit-Card-fraud-detection-dashboard.git
git push -u origin main

🧑‍💻 Author

Ogundiya Adebisi Michael

© 2024 | Data Analyst 

📧 Michaelopiii@gmail.com 

🌐 linkedin.com/in/ogundiyaa

