import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Streamlit App')

st.write("Here's our first attempt at using data to create a table")
st.write(pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
}))

if st.button('Say hello'):
  st.write('Why hello there!')
else:
  st.write('Goodbye :(')

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columms=['a', 'b', 'c'])

st.lint_chart(chart_data)
