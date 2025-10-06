import streamlit as st
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import os

# ==============================
# App Configuration
# ==============================
st.set_page_config(page_title="💳 Fraud Detection Dashboard", layout="wide")

MODEL_PATH = r"C:\Users\User\Desktop\ADIN PROJECT\Fraud_app\fraud_xgb_model.json"

# ==============================
# Load XGBoost Model
# ==============================
@st.cache_resource
def load_model():
    model = xgb.XGBClassifier()
    model.load_model(MODEL_PATH)
    return model

# Check model availability
if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found. Please run `train_model.py` first to generate fraud_xgb_model.json.")
    st.stop()

xgb_clf = load_model()

# ==============================
# Header
# ==============================
st.title("💳 Fraud Detection App")
st.markdown(
    """
    This interactive dashboard allows you to **analyze and detect potential fraudulent transactions** 
    using a trained XGBoost model.  
    Upload your dataset or use a sample to test the model in real-time.
    """
)

# ==============================
# Sidebar
# ==============================
with st.sidebar:
    st.header("📂 Data Input Options")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"], help="Upload a CSV file with transaction data.")

    st.markdown("### 📥 Or Download a Sample")
    sample_df = pd.DataFrame({
        'Time': [100, 200, 300],
        'V1': [0.1, -0.2, 0.05],
        'V2': [1.2, 0.4, -0.3],
        'V3': [0.3, -0.6, 0.2],
        'V4': [0.5, -0.1, -0.4],
        'V5': [1.1, -0.9, 0.7],
        'V6': [0.2, 0.1, -0.3],
        'V7': [-0.4, 0.6, 0.2],
        'V8': [0.7, -0.8, 0.4],
        'V9': [0.3, 0.2, -0.5],
        'V10': [0.5, -0.3, 0.1],
        'V11': [0.4, -0.1, -0.2],
        'V12': [0.9, -0.7, 0.3],
        'V13': [-0.3, 0.5, -0.1],
        'V14': [0.2, -0.4, 0.6],
        'V15': [0.8, 0.3, -0.2],
        'V16': [-0.5, 0.6, -0.4],
        'V17': [0.7, -0.1, 0.9],
        'V18': [0.1, -0.3, 0.2],
        'V19': [-0.2, 0.5, -0.6],
        'V20': [0.6, -0.5, 0.1],
        'V21': [-0.3, 0.7, -0.2],
        'V22': [0.4, 0.2, -0.8],
        'V23': [0.1, -0.1, 0.3],
        'V24': [-0.5, 0.4, 0.7],
        'V25': [0.6, -0.3, -0.2],
        'V26': [0.3, 0.1, -0.1],
        'V27': [-0.2, 0.5, -0.4],
        'V28': [0.4, -0.6, 0.8],
        'Amount': [120.5, 450.0, 99.99]
    })
    csv = sample_df.to_csv(index=False).encode("utf-8")
    st.download_button("📊 Download Sample Data", csv, "sample_fraud_data.csv", "text/csv")

    # ✅ Styled Developer Name
    st.markdown("---")
    st.markdown(
    """
    <div style='text-align: center; background-color:#333333; padding:10px; border-radius:8px;'>
        <p style='font-size:14px; color:#FFFFFF; margin:0;'>
            👨‍💻 <strong>Developed by<br>Ogundiya  Adebisi Michael</strong><br>
            <span style='font-size:12px;'>© 2024</span>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# Data Loading
# ==============================
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Data uploaded successfully! {df.shape[0]} rows and {df.shape[1]} columns loaded.")
    except Exception:
        st.error("⚠️ Data is not related to fraud transactions. Please check your file.")
        st.stop()
else:
    st.info("📂 Please upload your dataset or use the sample data.")
    st.stop()

# ==============================
# Preprocessing with error handling
# ==============================
try:
    # Drop 'Class' column if present
    if 'Class' in df.columns:
        df = df.drop(columns=['Class'])

    # Ensure correct feature order
    expected_features = list(xgb_clf.get_booster().feature_names)
    df = df[expected_features]

    # ==============================
    # Run Predictions
    # ==============================
    preds = xgb_clf.predict(df)
    probabilities = xgb_clf.predict_proba(df)[:, 1]

    df['Fraud_Probability'] = probabilities
    df['Prediction'] = np.where(preds == 1, "Fraudulent 💥", "Legit ✅")

except Exception:
    st.error("⚠️ Data is not related to fraud transactions. Please check your file.")
    st.stop()

# ==============================
# Display Results
# ==============================
st.subheader("🔍 Prediction Results")
st.dataframe(df.head(20))

# ==============================
# Key Metrics
# ==============================
st.subheader("📈 Model Insights")
fraud_count = (df['Prediction'] == "Fraudulent 💥").sum()
legit_count = (df['Prediction'] == "Legit ✅").sum()

col1, col2, col3 = st.columns(3)
col1.metric("🧠 Total Transactions", len(df))
col2.metric("🚨 Fraudulent", fraud_count)
col3.metric("✅ Legitimate", legit_count)

# ==============================
# Real-time Charts
# ==============================
fig = px.pie(
    names=["Fraudulent", "Legitimate"],
    values=[fraud_count, legit_count],
    title="Fraud vs Legit Transactions",
    color_discrete_sequence=["red", "green"]
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("© 2024 Ogundiya Michael Adebisi | Fraud Detection Dashboard")
