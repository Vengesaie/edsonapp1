import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.header("Edson Website")
# Generate random time series data
if st.button("Test this"):
  time_series = np.random.randn(100)

# Plot the time series
  plt.plot(time_series)
  plt.title("Random 100-Unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Value")
  st.pyplot(plt.gcf()) 

if st.button("Person Profile"):
  time_series = np.random.randn(100)

if st.button("Publications"):
  time_series = np.random.randn(100)

if st.button("Experience"):
  time_series = np.random.randn(100)
  

