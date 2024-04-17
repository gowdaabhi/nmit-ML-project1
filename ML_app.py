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

def prediction(Buying, Maint, Doors, Persons, Lug_boot, Safety):
  if Safety == 'med':
    safety == 1
  elif Safety == 'high':
    safety == 2
  elif Safety == 'low':
    safety == 3
  df =pd.DataFrame([Buying, Maint, Doors, Persons, Lug_boot, safety],columns=['buying','maint','doors','persons','persons','lug_boot','safety'])
  prediction =model.predict([Buying, Maint, Doors, Persons, Lug_boot, safety])
  return prediction

st.title('car Evalution Classification')
st.image("""data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEBISExITFRUVFRUVFRUVFhUVEhUVFRUWFhUXFhYYHSggGBolGxUVITEhJSkrLi4wFx8zRDMtNygtLisBCgoKDg0OGhAQGi0gHSUtLS0wLS0tLy0tLS0tLS0tLS0tLSstKy0tLS0tLS0tLS0tLS0tLS4tLS0tLS0tLS0tLf/AABEIAKgBLAMBEQACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAAAgMBBAUGBwj/xABBEAABAwIDAwcKAwcEAwAAAAABAAIDBBESITEFBlETFEFhcYGRFSJCUlOSobHB0TJi8AcjQ4Ki0vFyk7LhJDTC/8QAGgEBAAMBAQEAAAAAAAAAAAAAAAECAwQFBv/EADURAQACAQIEAwYFBAIDAQAAAAABAgMEERIhMVEFE0EUUmGhsdEicYGRwRUyQvAz4QY08SP/2gAMAwEAAhEDEQA/APhqAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgkxhJsASeAzKDZbs2U+gR/qIYfBxCrN6x6ta4clulZ/ZYdlPGrmA8Ll1u9gIUeZXut7Nk7MjZZ9rH/X/ap4690Tp8nZB2zXdDoz/OG/87JxR3R5OTsh5Pk4N99n3Tijujyr9gUEnq/Fv3UeZXut7Pl91kbPk4fFR5tO63sub3Um7Mf0lo7b/QJ5tO57Ll7Jv2S/ofC4ceVYz4SFp+CvFollOO0dYUVNBLGLvjcBoHW8w9jhke4qVGsgICAgICAgICAgICAgICAgICAgICAgICAgINijo3SE2sA0Xc45NaOJP0VbWivVpjxWyTy/WfSPzdTZ9fDE9rcDzHcCR7SBM5vpFoIsOpp7+Kztim/90/o7MWqx4OWOm895+3o93vTufhombQ2bLzumw3lu399FbVxa22Q9IWu3XMaVjTU+K1vFMs+kfP7vm52g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""")

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
  cal_eval=prediction(Buying, Maint, Doors, Persons, Lug_boot, Safety)
  st.success(f'The Evalution of Car: {cal_eval[0]}')
