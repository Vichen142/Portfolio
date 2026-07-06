import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Blinkit Analytics Case Study", page_icon="📊", layout="wide")

st.title("🛒 Blinkit Delivery Sales Performance Hub")
st.subheader("Advanced Data Cleaning (Excel) & BI Visualization Architecture")

st.write("---")

# --- EXECUTIVE SUMMARY ---
st.markdown("### 📋 Project Architecture & Objective")
st.write(
    """
    This project focuses on transforming raw, unorganized transactional grocery records from Blinkit 
    into an enterprise-grade performance monitoring system. The primary goal was to dissect revenue trends, 
    analyze structural outlet parameters (size, location tiers), and evaluate item velocity metrics to optimize distribution channels.
    """
)

# --- THE DATA ANALYST PIPELINE ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🛠️ Phase 1: Data Cleaning & Wrangling (Excel)")
    st.markdown(
        """
        - **Anomaly Rectification:** Handled massive data inconsistencies within categorical naming schemas (e.g., standardizing text variants like 'Low Fat', 'LF', and 'lowfat' into a unified segment tag).
        - **Missing Structural Imputations:** Calculated and populated missing records for item weights using conditional averages based on unified category keys.
        - **Structural Integrity Checks:** Managed extreme values and structural errors across 8,500+ record fields using advanced tabular filtering protocols.
        """
    )

with col2:
    st.markdown("### 📐 Phase 2: Data Modeling & Analytics (Power BI)")
    st.markdown(
        """
        - **Relational Data Modeling:** Established relational schemas connecting product SKUs directly to outlet operational metrics.
        - **DAX Measure Engineering:** Wrote custom Data Analysis Expressions (DAX) to dynamically calculate critical KPIs, including *Total Aggregated Sales*, *Average Ticket Values (MRP)*, and *Multi-Category Growth Multipliers*.
        - **User Experience Design:** Engineered interactive slicing mechanics enabling corporate stakeholders to filter operations instantly by location tier, business size, and category.
        """
    )

st.write("---")

# --- EMBEDDING / SHOWCASING WORK ---
st.markdown("### 🖼️ Live Interactive Dashboard Interface")

# --- IF USING OPTION A: SCREENSHOT DISPLAY ---
script_dir = os.path.dirname(os.path.abspath(__file__))
# Moves one level up from the pages folder to find the image in the root directory
project_root = os.path.dirname(script_dir)
image_path = os.path.join(project_root, "blinkit_dashboard.png")

if os.path.exists(image_path):
    st.image(image_path, caption="Blinkit Sales Analysis Dashboard Overview Profile (Engineered in Power BI Desktop)", use_container_width=True)
else:
    st.info("💡 Place a high-quality screenshot named 'blinkit_dashboard.png' in your project folder to display it here!")


# --- IF USING OPTION B: UNCOMMENT THE LINE BELOW TO EMBED AN INTERACTIVE POWER BI WEB LINK ---
# st.components.v1.html('<iframe title="Blinkit Report" width="100%" height="600" src="YOUR_PASTE_PUBLIC_POWER_BI_EMBED_URL_HERE" frameborder="0" allowFullScreen="true"></iframe>', height=600)

st.write("---")