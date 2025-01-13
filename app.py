import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Set Streamlit page configuration
st.set_page_config(page_title="Streamlit Demo", layout="wide")

# Header
st.title("Streamlit Demo with Random Data")

# Create some random data
num_rows = random.randint(50, 100)
data = {
    "Date": pd.date_range(start="2021-01-01", periods=num_rows, freq="D"),
    "Category": [random.choice(['A', 'B', 'C', 'D']) for _ in range(num_rows)],
    "Value": np.random.randn(num_rows).cumsum() + 50  # Cumulative sum to make it look like a trend
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
st.subheader("Random Data")
st.write(df)

# Chart: Line plot of the random "Value" over time
st.subheader("Line Plot of Random Values")
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Date", y="Value", ax=ax, hue="Category")
ax.set_title("Cumulative Values Over Time")
st.pyplot(fig)

# Slider to adjust the number of points to display
st.subheader("Adjust Number of Rows to Display")
num_display = st.slider("Select the number of rows to display", min_value=10, max_value=100, value=num_rows)
st.write(df.head(num_display))

# Button to generate a new dataset
if st.button("Generate New Data"):
    st.experimental_rerun()

# Select box for filtering data by category
category_filter = st.selectbox("Select Category to Filter Data", options=["All", "A", "B", "C", "D"])
if category_filter != "All":
    df = df[df["Category"] == category_filter]
st.write(f"Displaying data for Category: {category_filter}")
st.write(df)

# Display a number input for a custom threshold to filter the data
threshold = st.number_input("Enter a threshold to filter 'Value'", value=50, min_value=0)
filtered_df = df[df["Value"] > threshold]
st.write(f"Displaying values greater than {threshold}")
st.write(filtered_df)

# Footer
st.markdown("---")
st.write("Created with Streamlit | Demo with Random Data and Components")

