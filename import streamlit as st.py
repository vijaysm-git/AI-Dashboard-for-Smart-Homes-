import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Simulated appliance data
appliances = ["Air Conditioner", "Refrigerator", "Washing Machine", "TV", "Lights"]
usage = [random.randint(100, 2000) for _ in appliances]
df_usage = pd.DataFrame({
    "Appliance": appliances,
    "Current Usage (W)": usage
})

# Simulated AI tips
tips = [
    "Washing Machine has been idle for 2 hours – Turn off?",
    "TV is ON in an empty room – Consider turning it off.",
    "Lighting is at full brightness during daylight – Dim lights?"
]

# Simulated past 10-day usage & savings data
dates = pd.date_range(end=pd.Timestamp.today(), periods=10)
consumption = np.random.randint(400, 800, size=10)
savings = np.round(np.random.uniform(2, 10, size=10), 2)
df_trends = pd.DataFrame({
    "Date": dates,
    "Energy Usage (kWh)": consumption,
    "Estimated Savings ($)": savings
}).set_index("Date")

# Streamlit UI
st.set_page_config(page_title="AI Smart Energy Dashboard", layout="wide")
st.title("🏠 AI for Smart Energy Conservation in Homes")

# Live Usage Section
st.header("📊 Live Appliance Usage")
st.dataframe(df_usage, use_container_width=True)
st.bar_chart(df_usage.set_index("Appliance"))

# AI Recommendations
st.header("🧠 AI-Generated Energy Saving Tips")
for tip in tips:
    st.warning(tip)

# Trends and Savings
st.header("📈 Energy Consumption Trends")
st.line_chart(df_trends[["Energy Usage (kWh)"]])


# Simulate optimization
if st.button("🔄 Optimize Energy Usage Now"):
    with st.spinner("Adjusting home devices based on AI analysis..."):
        time.sleep(2)
    st.success("✅ Optimizations Applied: HVAC adjusted, idle appliances turned off.")
