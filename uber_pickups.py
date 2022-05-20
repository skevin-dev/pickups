# -*- coding: utf-8 -*-
"""
@author: Shyaka Kevin 
"""
# -*- coding: utf-8 -*-
"""
@author: Shyaka Kevin 
"""

import streamlit as st 
import pandas as pd 
import numpy as np

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('loading data...')

data = load_data(10000)

data_load_state.text('done! (using st.cache)')

st.title('uber pickups in NYC')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
    
if st.checkbox('histogram'):
    st.title('Number of pickups by hour')
    st.bar_chart(np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0])

if st.checkbox('all pickups map'):
    st.subheader('Map of all pickups')
    how_to_filter = st.slider('hour',0,23,17)
    st.map(data[data[DATE_COLUMN].dt.hour==how_to_filter])

  