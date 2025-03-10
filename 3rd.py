import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("university_student_dashboard_data (1).csv")

# Streamlit UI
st.title("📊 University Admissions & Student Satisfaction Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
term_filter = st.sidebar.selectbox("Select Term", df["Term"].unique())
department_filter = st.sidebar.selectbox("Select Department", ["All", "Engineering", "Business", "Arts", "Science"])

# Filter Data
filtered_df = df[df["Term"] == term_filter]
if department_filter != "All":
    filtered_df = filtered_df[filtered_df[f"{department_filter} Enrolled"] > 0]

# Key Metrics
st.header("Key Metrics")
st.metric("Total Applications", filtered_df["Applications"].sum())
st.metric("Total Admissions", filtered_df["Admitted"].sum())
st.metric("Total Enrollments", filtered_df["Enrolled"].sum())

# Retention Rate Trends
st.header("Retention Rate Trends")
fig, ax = plt.subplots()
sns.lineplot(data=filtered_df, x="Year", y="Retention Rate (%)", marker="o", ax=ax)
plt.title("Retention Rate Trends Over Time")
st.pyplot(fig)

# Student Satisfaction Scores
st.header("Student Satisfaction Scores")
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x="Year", y="Student Satisfaction (%)", ax=ax)
plt.title("Student Satisfaction Trends Over the Years")
st.pyplot(fig)

# Enrollment Breakdown by Department
st.header("Enrollment Breakdown by Department")
departments = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
enrollment_data = filtered_df[departments].sum().reset_index()
enrollment_data.columns = ["Department", "Enrolled"]
fig, ax = plt.subplots()
sns.barplot(data=enrollment_data, x="Department", y="Enrolled", palette="Set3", ax=ax)
plt.title("Enrollment Breakdown by Department")
st.pyplot(fig)

# Comparison Between Spring and Fall Term Trends
st.header("Spring vs. Fall Term Trends")
fig, ax = plt.subplots()
sns.barplot(data=df[df["Term"].isin(["Spring", "Fall"])], x="Term", y="Enrolled", hue="Term", ax=ax, palette="pastel")
plt.title("Enrollment Comparison Between Spring and Fall Terms")
st.pyplot(fig)

# Comparison Between Departments (Retention Rates and Satisfaction Levels)
st.header("Department Comparison: Retention Rates & Satisfaction")
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Retention Rate by Department
for department in departments:
    sns.lineplot(data=filtered_df, x="Year", y=department, marker="o", ax=ax[0], label=department)
ax[0].set_title("Retention Rate Trends by Department")
ax[0].set_ylabel("Retention Rate (%)")
ax[0].legend(title="Department")

# Satisfaction Score by Department
sns.barplot(data=filtered_df.melt(id_vars=["Year"], value_vars=departments, var_name="Department", value_name="Satisfaction (%)"),
            x="Year", y="Satisfaction (%)", hue="Department", ax=ax[1])
ax[1].set_title("Satisfaction Levels by Department")
ax[1].legend(title="Department")

st.pyplot(fig)

# Key Findings and Actionable Insights
st.header(" Key Findings & Actionable Insights")
st.write("**Insights:**")
st.write("- Retention rates across departments have shown some ups and downs. Engineering, in particular, has been struggling, indicating a clear need for support programs to help students stay on track.")
st.write("- Student satisfaction scores have been quite the rollercoaster ride over the years. It’s crucial to keep a close eye on these scores and continuously work on making improvements.")
st.write("- The Engineering department seems to be the most popular choice among students, with the highest number of enrollments. This means we might need to allocate more resources to support the growing number of students.")
st.write("- Interestingly, the Spring term sees higher enrollments compared to the Fall term. It’s worth looking into why this is happening and addressing any potential issues causing this imbalance.")
