#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from pathlib import Path
from IPython import get_ipython
import streamlit as st

# text input
string = st.text_input(
    'Movie title', placeholder='write down the title of your favorite movie'
)

if string:
    st.text('Your answer is '+string)
    
# password 인자 활용
string = st.text_input(
    'Movie title',
    placeholder='write down the title of your favorite movie',
    type='password'
)

if string:
    st.text('Your answer is '+string)

# file uploader
file = st.file_uploader(
    'Choose a file', type='csv', accept_multiple_files=False
)
if file is not None:
    df = pd.read_csv(file)
    st.write(df)

