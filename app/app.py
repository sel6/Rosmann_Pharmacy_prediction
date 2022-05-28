import streamlit as st
import pandas as pd
import numpy as np

def app1():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:2rem;border-radius:0.8rem;'>Rossmann Pharmaceuticals</p>", unsafe_allow_html=True)
    
        st.markdown("<p style='font-size:1.8rem'>With about 56,200 employees and over 4000 locations across Europe, Dirk Rossmann GmbH (commonly known as Rossmann) is one of Europe's major drugstore companies.</p>", unsafe_allow_html=True)

        st.markdown("<p style='font-size:1.8rem'>The Rosemann pharmaceutical firm can examine sales estimates for its stores six weeks in advance, as well as projected patterns, thanks to this app, which is an end-to-end solution.</p>",unsafe_allow_html=True)

def app3():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Insights inferred from the data</p>", unsafe_allow_html=True)
    
        st.markdown("<p style='font-size:1.8rem'>The data has a number of important attributes that can be used to get insight into retail sales. The following conclusions can be drawn based on the exploratory data analysis: The volume of sales is proportional to the number of clients.</p>", unsafe_allow_html=True)


def app4():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Prediction query page</p>", unsafe_allow_html=True)
    
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if st.button("Process"):
          if data_file is not None:
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
            st.write(file_details)

            df = pd.read_csv(data_file)
            st.dataframe(df)

def app5():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Prediction query page</p>", unsafe_allow_html=True)
    
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if st.button("Process"):
          if data_file is not None:
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
            st.write(file_details)

            df = pd.read_csv(data_file)
            st.dataframe(df)

app4()
app1()
app5()
app3()