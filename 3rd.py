!pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("university_student_dashboard_data.csv")

# Streamlit UI
st.title("📊 University Admissions & Student Satisfaction Dashboard")

# Show overall statistics
st.sidebar.header("Filters")
term_filter = st.sidebar.selectbox("Select Term", df["term"].unique())

filtered_df = df[df["term"] == term_filter]

# Key Metrics
st.metric("Total Applications", filtered_df["applications"].sum())
st.metric("Total Admissions", filtered_df["admissions"].sum())
st.metric("Total Enrollments", filtered_df["enrollments"].sum())

# Retention Rate
fig, ax = plt.subplots()
sns.lineplot(data=df, x="year", y="retention_rate", hue="department", marker="o", ax=ax)
plt.title("Retention Rate Trends")
st.pyplot(fig)

# Satisfaction Scores
fig, ax = plt.subplots()
sns.barplot(data=df, x="year", y="satisfaction_score", hue="department", ax=ax)
plt.title("Student Satisfaction Trends")
st.pyplot(fig)

st.write("📌 **Insights:** Retention rates have fluctuated across departments. Engineering has the lowest retention, indicating a need for support programs.")

