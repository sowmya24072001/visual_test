import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("university_student_dashboard_data (1).csv")

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
# If you want to plot retention rate for each department, you need to use the columns that represent departments
departments = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
for department in departments:
    sns.lineplot(data=df, x="Year", y=department, marker="o", ax=ax, label=department)
plt.title("Retention Rate Trends by Department")
ax.set_ylabel("Retention Rate (%)")
ax.legend(title="Department")
st.pyplot(fig)

# Satisfaction Scores
fig, ax = plt.subplots()
sns.barplot(data=df, x="Year", y="Student Satisfaction (%)", ax=ax)
plt.title("Student Satisfaction Trends")
st.pyplot(fig)

st.write("📌 **Insights:** Retention rates have fluctuated across departments. Engineering has the lowest retention, indicating a need for support programs.")
