import math as math
import os,sys,errno,configparser,time,warnings

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")

st.title ("XUR Work Space")

tab1, tab2, tab3 ,tab4= st.tabs(["app","device","ML","FFXIV launcher settings"])
with tab1:
    st.title ("APP")
    with st.expander ("EFLORE Settings"):
        model_name= st. text_input('New Contents Name')
        col1,col2 = st. columns (2)
        with col1:
            optimizer = st.selectbox(
            'optimizer method',
            ('', 'adam', 'Nadam' 'SGD', 'RMSprop', 'AdamW', 'Adade Ita', 'Adagrad', 'Adamax', 'Adafactor', 'Ftrl'))
        with col2:
            loss = st.selectbox(
            'loss function',
            ('', 'adam', 'Nadam' 'SGD', 'RMSprop', 'AdamW', 'Adade Ita', 'Adagrad', 'Adamax', 'Adafactor', 'Ftrl'))

        epoch = st.slider ('epoch', 0, max_value=20)
        batch_size= st.slider('batch_size',min_value=28, max_value=1024)
        st.checkbox ('use GPU')
        st.checkbox ('use parallelization')

    col3, col4= st.columns ([1,5])
    with col3:
        st.write("EFILDIS 5X-3")
    with col4:
        st.write(f'<span>optimizer : </span>'+ '<span style="color:green">' + optimizer +'</span>',unsafe_allow_html=True)
        st.write(f'<span>optimizer : </span>'+ '<span style="color:green">' + optimizer +'</span>',unsafe_allow_html=True)
        st.write(f'<span>optimizer : </span>'+ '<span style="color:green">' + optimizer +'</span>',unsafe_allow_html=True)
        st.write(f'<span>optimizer : </span>'+ '<span style="color:green">' + optimizer +'</span>',unsafe_allow_html=True)
with tab2:
    pass
with tab3:
    pass
with tab4:
    pass
