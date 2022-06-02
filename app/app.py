import streamlit as st
import pandas as pd
import numpy as np
import pickle

def welcome():
    st.markdown("<h1 style='padding:2rem;text-align:center; background-color:green;color:black;font-size:1.8rem;border-radius:0.8rem;'>Rosmann Pharmaceuticals</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='font-famly:Arial, Helvetica, sans-serif;'>Rossmann is one of the largest drug store chains in Europe with around 56,200 employees and more than 4000 stores. In 2019 Rossmann had more than €10 billion turnover in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.</p1>", unsafe_allow_html=True)
    st.image('image/rosmann.jpg')


def app_purpose():
    st.markdown("<h2 style='padding:2rem;text-align:left;color:white;font-size:1.8rem;border-radius:0.5rem;'>About</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("""
    This app was developed to serve an end-to-end product 
    that delivers prediction that helps The finance team to forecast sales in all their stores across several cities six weeks ahead of time. 
    """)
   

def apk():
    model = pickle.load(open("models/random_forest2.pkl", 'rb'))
    scaler = pickle.load(open("models/scaled2022-05-28-09-32-07.pkl", 'rb'))
    st.markdown("<h3 style='padding:2rem;text-align:left;color:white;font-size:1.8rem;border-radius:0.5rem;'>Sales Prediction</h3>", unsafe_allow_html=True)
    st.write("By entering input parameters, the model outputs predicted sales amount and customer number")
    data = pd.DataFrame()

    Store = st.number_input("Store ID", min_value=1, max_value=1115)
    uploaded = st.file_uploader("Choose file")
    dist = st.number_input("Competition Distance", min_value=1, max_value=20000)
    StoreType = 0
    StoreTypes = st.radio(
    "Store Type",
    ('a', 'b', 'c', 'd'))

    if StoreTypes == 'a':
        StoreType = 0
    elif StoreTypes == 'b':
        StoreType = 1
    elif StoreTypes == 'c':
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



    calculate = st.button('Calculate')
    if ((uploaded is not None) and (calculate)):
        input = pd.read_csv(uploaded)
        st.write(input)
        data = input.loc[:,['Month', 'WeekOfYear', 'DayOfWeek', 'DayOfMonth', 'Promo','Open']]
        st.write(data)
        
        data.insert(2, 'Assortment', Assortment)
        data.insert(3, 'StoreType', StoreType)
        data.insert(8, "Store", Store)
        data.insert(9, "CompDist", dist)
        #input_data = minmax_scale(np.array(input_data))
        
        st.write(data.head())
        prediction = model.predict(data)
        data.insert(0, "Sales", prediction)
        rev_sca = scaler.inverse_transform(data)
        rev_sca = pd.DataFrame(rev_sca)
        st.write(rev_sca.head())
        st.write("Sales Prediction is: {}".format ( rev_sca.loc[0,0]))

if __name__=="__main__":
    welcome()
    app_purpose()
    apk()
