import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("university_student_dashboard_data (1).csv")

# Streamlit UI
st.title("📊 University Admissions & Student Satisfaction Dashboard")

# Show overall statistics
st.sidebar.header("Filters")
term_filter = st.sidebar.selectbox("Select Term", df["Term"].unique())

filtered_df = df[df["Term"] == term_filter]

# Key Metrics
st.metric("Total Applications", filtered_df["Applications"].sum())
st.metric("Total Admissions", filtered_df["Admitted"].sum())
st.metric("Total Enrollments", filtered_df["Enrolled"].sum())

# Retention Rate
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Year", y="Retention Rate (%)", hue="department", marker="o", ax=ax)
plt.title("Retention Rate Trends")
st.pyplot(fig)

# Satisfaction Scores
fig, ax = plt.subplots()
sns.barplot(data=df, x="Year", y="Student Satisfaction (%)", hue="department", ax=ax)
plt.title("Student Satisfaction Trends")
st.pyplot(fig)

st.write("**Insights:** Retention rates have fluctuated across departments. Engineering has the lowest retention, indicating a need for support programs.")
