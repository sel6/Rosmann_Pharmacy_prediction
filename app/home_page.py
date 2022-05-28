import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sys
sys.path.insert(1, '../models')

def welcome():
    st.header('Rosmann Pharmaceuticals')
    st.write('---')
    st.write(
        """
        Rossmann is one of the largest drug store chains in Europe with around 56,200 employees
        and more than 4000 stores. In 2019 Rossmann had more than €10 billion turnover in Germany,
        Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.
        
        """
    )
    st.image('image/rosmann.jpg')

def app_purpose():
    st.header("About")
    st.write("---")
    st.write("""
    This app was developed to serve an end-to-end product 
    that delivers prediction that helps The finance team to forecast sales in all their stores across several cities six weeks ahead of time. 
    """)

def apk():
    st.header("Rosmanns Sales Prediction")
    st.caption("By entering input parametrs, this model outputs predicted sales amount and customer number.")
    model = pickle.load(open("models/random_forest2.pkl", 'rb'))
    scaler = pickle.load(open("models/scaled2022-05-28-09-32-07.pkl", 'rb'))

    DayOfMonth = 3
    DayOfWeek = 4
    WeekOfYear = 30
    Month = 7
    upload = 2


    dte= st.radio(
    "Date",
    ('Enter', 'Upload'))

    if dte == 'Upload':
        upload = 1
    else:
        upload = 0

    with st.form(key='my_form'): 
        if(upload == 1):
            uploaded = st.file_uploader("Choose file")
            if uploaded != None:
            
                df = pd.read_csv(uploaded)
                st.write(df)
                DayOfMonth = df.iloc[0,1]
                DayOfWeek = df.iloc[0,2]
                WeekOfYear = df.iloc[0,3]
                Month = df.iloc[0,4]
        
        elif(upload == 0):
            Month = st.number_input("Month", min_value=1, max_value=12)
            DayOfMonth = st.number_input("Day of Month", min_value=1, max_value=31)
            DayOfWeek = st.number_input("Day of Week", min_value=1, max_value=7)
            WeekOfYear = st.number_input("Week of Year", min_value=1, max_value=52)
            
        Open = 0
        status = st.radio(
        "Store Status",
        ('Open', 'Closed'))

        if status == 'Open':
            Open = 1
        else:
            Open = 0

        
        dist = st.number_input("Competition Distance", min_value=1, max_value=20000)
        Store = st.number_input("Store ID", min_value=1, max_value=1115)
        Promo = 0
        Prom = st.radio(
        "Promotion",
        ('Yes', 'No'))

        if Prom == 'Yes':
            Promo = 1
        else:
            Promo = 0

        StoreType = 0
        StoreTypes = st.radio(
        "Store Type",
        ('a', 'b', 'C', 'd'))

        if StoreTypes == 'a':
            StoreType = 0
        elif StoreTypes == 'b':
            StoreType = 1
        elif StoreTypes == 'C':
            StoreType = 2
        else:
            StoreType = 3

        Assortment = 0
        assort = st.radio(
        "Assortment Type",
        ('Basic', 'Extra', 'Extended'))

        if assort == 'Basic':
            Assortment = 0
        elif assort == 'Extra':
            Assortment = 1
        else:
            Assortment = 2

        submit_button = st.form_submit_button(label='Submit')
    
    input_data = [0, Month, Assortment, StoreType, WeekOfYear, DayOfWeek, DayOfMonth, Promo, Store, dist, Open]
    input_keys = ["Sales", "Month", "PromoInterval", "Assortment", "StoreType", "WeekOfYear", "DayOfWeek", "DayOfMonth", "Promo", "Store", "dist","Open"]
    input_dict = {}
    for i in range(len(input_data)):
        input_dict[input_keys[i]] = [input_data[i]]
        
    input_df = pd.DataFrame(input_dict)
    if st.button('Calculate'):
        
        scaled_df = scaler.transform(input_df)
        scaled_df = scaled_df[:,1:]
        prediction = model.predict(scaled_df)
        scaled_arr2 = pd.DataFrame(scaled_df)
        scaled_arr2.insert(0, 11, prediction[0])
        sca_reverse = scaler.inverse_transform(scaled_arr2)
        sca_reverse = pd.DataFrame(sca_reverse)
        st.write(sca_reverse)
        st.write("Sales Prediction: {}".format ( sca_reverse.loc[0,0]))

welcome()
app_purpose()
apk()