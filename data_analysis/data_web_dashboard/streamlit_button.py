#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from pathlib import Path
from IPython import get_ipython
import streamlit as st
# button
def button_write():
    st.write('button activated')

# 클릭 시 if문을 실행
st.button('Reset', type='primary', key="3")
if st.button('activate', key="4"):
    st.write('button activated')
    
# checkbox
active = st.checkbox('I agree', key="1")

if active:
    st.text('Great!')
    
# checkbox on_change 인자 활용
def checkbox_write():
    st.write('Great!')

st.checkbox('I agree', on_change=checkbox_write)

# toggle
toggle = st.toggle(
    'Turn on the switch!', value=True
)

if toggle:
    st.text('Switch is turned on!')
else:
    st.text('Switch is turned off!')


