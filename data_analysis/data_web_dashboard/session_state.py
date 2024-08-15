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

i = 0

st.header('Session state example1')

plus_one = st.button(
    label='+1',
)

if plus_one:
    i += 1

st.text('i = {}'.format(i))

# session state에 변수 저장
st.header('Session state example2')


if 'i' not in st.session_state:
    st.session_state['i'] = 0

plus_one = st.button(
    label='+1',
    key='btn_plus1'
)

if plus_one:
    st.session_state['i'] += 1
    
st.text('i = {}'.format(st.session_state['i']))

# session state에 변수 저장2
st.header('Session state example3')

st.slider(
    label='Can I remember this number?',
    min_value=1, max_value=10, step=1,
    key='remember_slider'
)

st.text('Result is... {}'.format(st.session_state['remember_slider']))

# 캐싱
@st.cache_data
def expensive_computation(a, b):
    st.text('Result: {}'.format(a+b))

result = st.button(
    'Calculate',
    on_click=expensive_computation, args=(23, 5,)
)

