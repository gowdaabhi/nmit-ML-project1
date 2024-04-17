import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier
# loading up the classification model we created

model =DecisionTreeClassifier(criterion='gini',max_depth=8, min_samples_leaf=5, random_state=0)

model =joblib.load('finalized_model.joblib')
# caching the model for faster loading

@st.cache

# define the predection function

def predict(Buying, Maint, Doors, Persons, Lug_boot, Safety):
  if Safety == 'med':
    safety == 1
  elif Safety =='high':
    safety == 2
  elif Safety == 'low':
    safety = 3
  df =pd.DataFrame([Buying, Maint, Doors, Persons, Lug_boot, Safety],columns=['buying','maint','doors','persons','persons','lug_boot','safty'])
  prediction =model.predict([Buying, Maint, Doors, Persons, Lug_boot, Safety])
  return prediction

st.title('car Evalution Classification')
st.image("""https://www.google.com/imgres?q=Lamborghini.jpg&imgurl=https%3A%2F%2Fimgd.aeplcdn.com%2F1920x1080%2Fec%2F79%2F85%2F9802%2Fimg%2Fol%2FLamborghini-Aventador-Front-view-52648.jpg%3Fv%3D201711021421%26q%3D80%26q%3D80&imgrefurl=https%3A%2F%2Fwww.carwale.com%2Flamborghini-cars%2Faventador%2F&docid=UOa8oQzM8XAQ-M&tbnid=OkgWn2iH4EilGM&vet=12ahUKEwjPgIKC2ciFAxXO8zgGHZtzBQMQM3oECEEQAA..i&w=1920&h=1080&hcb=2&ved=2ahUKEwjPgIKC2ciFAxXO8zgGHZtzBQMQM3oECEEQAA""")

st.header('Enter the Information of the Car:')

st.text("vhigh = 1 high = 2 med = 3 low = 4")

Buying = st.number_input('buying:', min_value=1, max_value=4, value=1)

st.text("vhigh = 1 high = 2 med 3 low = 4")

Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)

st.text("2-Doors = 1 3-Doors 2 4-Doors = 3 5more = 4")

Doors=st.number_input('doors:', min_value=1, max_value=4, value=1)

st.text("2-persons = 1 4-persons = 2 more = 3 ")

Persons=st.number_input('persons:', min_value=1, max_value=3, value=1)

st.text("small 1 med 2 big = 3")

Lug_boot=st.number_input('lug_boot:', min_value=1, max_value=3, value=1)

Safety=st.radio('safety:', ('med', 'high', 'low'))

if st.button('submit_car_Infos'):
  cal_eval=predict(Buying, Maint, Doors, Persons, Lug_boot, Safety)
  st.success(f'The Evalution of Car: {cal_eval[0]}')
