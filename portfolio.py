import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Opeyemi Henry | Portfolio", page_icon="📊", layout="wide")

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)

with col2:
    st.title("Opeyemi Henry")
    st.subheader("Data Analyst & Machine Learning Engineer")
    st.write("📍 Lagos, Nigeria")
    st.write(
        """
        I build interactive, end-to-end machine learning solutions and data pipelines 
        that turn raw information into actionable business insights. From data wrangling 
        and predictive modeling to deploying live user interfaces, I bridge the gap 
        between complex algorithms and practical application.
        """
    )
    st.markdown("🔗 [LinkedIn](https://linkedin.com) | 💻 [GitHub](https://github.com/Vichen142)")

# --- DOWNLOAD RESUME PROTOCOL ---
# Dynamically locate the folder where portfolio.py is running
current_dir = os.path.dirname(os.path.abspath(__file__))
# Target the PDF file sitting right next to it
resume_path = os.path.join(current_dir, "HENRY_OPEYEMI_FlowCV_Resume_2026-07-02.pdf")

try:
    with open(resume_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="📥 Download Resume (PDF)",
        data=PDFbyte,
        file_name="HENRY_OPEYEMI_Resume.pdf",
        mime="application/pdf",  # Updated to exact PDF MIME type
    )
except FileNotFoundError:
    st.warning("⚠️ Resume file path not found. Please verify that the PDF file is inside your project folder.")

st.write("---")

# --- SKILLS MATRIX ---
st.header("🛠️ Technical Toolkit")

col3, col4, col5 = st.columns(3)
with col3:
    st.markdown("### **Languages & Databases**")
    st.markdown("- Python\n- SQL\n- Java")
with col4:
    st.markdown("### **Data Analysis & Vizualization**")
    st.markdown("- Power BI\n- Advanced Excel\n- Pandas & NumPy\n- Seaborn & Matplotlib")
with col5:
    st.markdown("### **Machine Learning & Ops**")
    st.markdown("- Scikit-Learn\n- Predictive Modeling\n- Streamlit Deployment\n- Git & GitHub")

st.write("---")

# --- PROJECTS & EXPERIENCE SECTION ---
st.header("🚀 Featured Projects & Experience")

# Project 1: Customer Churn Predictive Engine
with st.container():
    st.subheader("💳 Customer Churn Predictive Engine")
    st.write(
        """
        Developed an end-to-end machine learning pipeline to detect customer churn status. 
        Engineered features, handled massive class imbalance using advanced sampling techniques, and trained 
        highly optimized classification models using Python and Google Colab to maximize recall and precision.
        """
    )
    # CLICKING THIS BUTTON SWITCHES PAGES INTERNALLY
    if st.button("🚀 Launch Interactive churn Model", key="fraud_btn"):
        st.switch_page("pages/Customer_Churn_Predictive_Engine.py")

st.write("")

# Project 2: blinkit Analytics Dashboard
with st.container():
    st.subheader("📊 Blinkit Interactive Analytics Dashboard")
    st.write(
        """
        Designed and deployed a highly responsive interactive web dashboard using Streamlit. 
        The application processes structured datasets, dynamically updates key metrics based on user filtering, 
        and visualizes operational data trends using optimized charting libraries.
        """
    )
    # CLICKING THIS BUTTON SWITCHES PAGES INTERNALLY
    if st.button("📈 Launch Live Analytics Dashboard", key="dash_btn"):
        st.switch_page("pages/2_Analytics_Dashboard.py")

st.write("")

# Project 3: The Upcycle Design Lab
with st.container():
    st.subheader("🌱 The Upcycle Design Lab (Social Impact & Operations)")
    st.write(
        """
        A data-informed project designed for the Millennium Fellowship aimed at addressing youth unemployment 
        through community waste transformation. Focused on creating systematic frameworks for mapping local environmental 
        waste issues and tracking community metrics.
        """
    )

st.write("")

# Project 4: Ecoservants
with st.container():
    st.subheader("📉 Volunteer Data Analyst — Ecoservants")
    st.write(
        """
        Served as a volunteer data analyst, cleaning environmental datasets, identifying key localized insights, 
        and building exploratory data analysis structures to support community-driven initiatives.
        """
    )

st.write("---")