#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from IPython import get_ipython
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
from pathlib import Path

# sidebar
st.title('This is main page')

with st.sidebar:
    st.title('This is sidebar')
    side_option = st.multiselect(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship','Bicycle'],
    placeholder='select transportation'
    )

image_path2 = Path('./images/background.jpg')
image_path3 = Path('./images/tree.jpg')
# column 이해
img2 = Image.open(image_path2)
img3 = Image.open(image_path3)

st.header('Lemonade')
st.image(img2, width=300, caption='Image from Unsplash')

st.header('Cocktail')
st.image(img3, width=300, caption='Image from Unsplash')

# column 활용
col1, col2 = st.columns(2)

with col1:
    st.header('Lemonade')
    st.image(img2, width=300, caption='Image from Unsplash')

with col2:
    st.header('Cocktail')
    st.image(img3, width=300, caption='Image from Unsplash')
    
# tab
tab1, tab2 = st.tabs(['Table','Graph'])
data_path = Path('../../data_analysis_lect/datasets/medical_cost/medical_cost.csv')
df = pd.read_csv(data_path)
df = df.query('region == "northwest"')

with tab1:
    st.table(df.head(5))

with tab2:
    fig = px.scatter(
        data_frame=df, x='bmi', y='charges'
    )
    st.plotly_chart(fig)
    
# expander
df = pd.read_csv(data_path)
df = df.query('region == "northwest"')

fig = px.scatter(
        data_frame=df, x='bmi', y='charges'
    )
st.plotly_chart(fig)
    
with st.expander("See datatable"):
    st.table(df.head(5))

