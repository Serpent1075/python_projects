#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from pathlib import Path
from IPython import get_ipython
import streamlit as st
# slider
score = st.slider('Your score is...', 0, 100, 1)
st.text('Score: {}'.format(score))

# 날짜 및 시간 slider
from datetime import time

start_time, end_time = st.slider(
    'Working time is...',
    min_value=time(0), max_value=time(23),
    value=(time(8), time(18)),
    format='HH:mm'
)
st.text('Working time: {}, {}'.format(start_time, end_time))
