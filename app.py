# app.py
import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
# --- Layout ---
st.set_page_config(page_title="Attrition Dashboard", layout="wide")
st.title("📊 Employees Attrition Dashboard")
# --- Load model dan data ---
@st.cache_resource
def load_model():
    return pickle.load(open("model_attrition.pkl", "rb"))

@st.cache_data
def load_data():
    return pd.read_csv("employee_data.csv")

model = load_model()
df = load_data()

# --- Preprocessing untuk Visualisasi ---
df_viz = df.copy()
df_viz.dropna(subset=["Attrition"], inplace=True)
df_viz["Attrition"] = df_viz["Attrition"].astype(int)

# Custom grouping (agar mirip Looker)
def bin_age(age):
    if age < 30:
        return "Young Age"
    elif age < 40:
        return "Middle Age"
    elif age < 55:
        return "Pre-retirement Age"
    else:
        return "Retirement Age"

def bin_experience(years):
    if years >= 15:
        return "Senior Employee"
    elif years >= 8:
        return "Mid-level Employee"
    elif years >= 3:
        return "Junior Employee"
    else:
        return "Fresh Graduate"

def bin_salary(income):
    if income < 3000:
        return "Low Salary"
    elif income < 7000:
        return "Medium Salary"
    else:
        return "High Salary"

df_viz["Age Group"] = df_viz["Age"].apply(bin_age)
df_viz["Experience Group"] = df_viz["TotalWorkingYears"].apply(bin_experience)
df_viz["Salary Group"] = df_viz["MonthlyIncome"].apply(bin_salary)

# --- SECTION 3: Prediksi Individual ---
st.header("🔎 Predict Employee Attrition")
emp_id = st.text_input("Masukkan Employee ID:")

if emp_id:
    if emp_id.isdigit() and int(emp_id) in df['EmployeeId'].values:
        emp_id = int(emp_id)
        data_karyawan = df[df['EmployeeId'] == emp_id].copy()
        st.subheader("📋 Data Karyawan")
        st.dataframe(data_karyawan)

        drop_cols = ['EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours', 'Attrition']
        data_model = data_karyawan.drop(columns=drop_cols, errors="ignore")

        prediction = model.predict(data_model)[0]
        prob = model.predict_proba(data_model)[0][1]

        st.subheader("📊 Hasil Prediksi")
        hasil = "Keluar ❌" if prediction == 1 else "Tetap ✅"
        warna = "red" if prediction == 1 else "green"
        st.markdown(f"**Status Prediksi:** <span style='color:{warna}; font-size:24px'>{hasil}</span>", unsafe_allow_html=True)
        st.markdown(f"**Probabilitas keluar:** `{prob:.2%}`")
    else:
        st.warning("❗ Employee ID tidak ditemukan atau salah format.")

# --- SECTION 1: Overview Charts ---
st.header("🔍 Overview of Employees Leaving")

col1, col2, col3 = st.columns(3)
with col1:
    fig1, ax1 = plt.subplots()
    df_viz['MaritalStatus'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1, labels=["Single", "Married", "Divorced"])
    ax1.set_title("Status")
    ax1.set_ylabel("")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    df_viz['Gender'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2)
    ax2.set_title("Gender")
    ax2.set_ylabel("")
    st.pyplot(fig2)

with col3:
    fig3, ax3 = plt.subplots()
    df_viz['OverTime'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax3)
    ax3.set_title("Over Time")
    ax3.set_ylabel("")
    st.pyplot(fig3)

# --- SECTION 2: Grouped Bar Charts ---
st.header("📚 Attrition by Group Features")

def plot_bar_grouped(feature, title):
    plt.figure(figsize=(6, 4))
    plot_data = df_viz.groupby([feature, "Attrition"]).size().unstack(fill_value=0)
    plot_data.rename(columns={0: "No", 1: "Yes"}, inplace=True)
    plot_data.plot(kind="bar", stacked=False, color=["skyblue", "salmon"])
    plt.title(title)
    plt.ylabel("Count")
    st.pyplot(plt.gcf())
    plt.close()

bar1, bar2 = st.columns(2)
with bar1:
    plot_bar_grouped("Age Group", "Age Group vs Attrition")
    plot_bar_grouped("WorkLifeBalance", "Work-Life Balance vs Attrition")

with bar2:
    plot_bar_grouped("Experience Group", "Experience Group vs Attrition")
    plot_bar_grouped("Salary Group", "Salary Group vs Attrition")

