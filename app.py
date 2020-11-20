from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('House')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo.jpg')
    image_hospital = Image.open('House.jpg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict housing  charges')


    st.sidebar.image(image_hospital)





    st.title("Housing Charges Prediction App")

    if add_selectbox == 'Online':

        bedrooms = st.number_input('Bedrooms', min_value=0.0, max_value=9.0, value=0.0)
        bathrooms = st.number_input('Bathrooms', min_value=0.0, max_value=9.0, value=0.0)
        sqft_living = st.text_input('Sqft_living,put a value in 4digit(3720)')
        sqft_lot = st.text_input('Sqft_lot(e.g 15084)')
        floors = st.number_input('Floors', min_value=0.0, max_value=9.0, value=0.0)
        waterfront = st.number_input('Waterfront', min_value=0, max_value=9, value=0)
        view = st.number_input('View', min_value=0, max_value=9, value=0)
        condition = st.number_input('Condition', min_value=0, max_value=9, value=0)
        sqft_above = st.text_input('Sqftabove(e.g 1234 )')
        sqft_basement = st.text_input('Sqftbasement(e.g 230 or 1234)')
        yr_built = st.text_input('Year can be 0 and start from 1920 and end 2009')
        yr_renovated =st.selectbox('Year', range(1992, 2005))
        city = st.selectbox('City', ["Renton", "Seattle","Bellevue","Redmond","Kirkland","Issaquah","Kent","Auburn","Sammamish","Federal Way",
        "Shoreline","Shoreline","Maple Valley","Mercer Island","Burien","Snoqualmie","Kenmore","Des Moines","North Bend",
        "Covington","Duvall","Lake Forest Park","Newcastle","Bothell","Vashon","SeaTac","Tukwila","Enumclaw","Carnation","Normandy Park","Medina","Fall City",
        "Clyde Hill","Black Diamond","Pacific","Algona","Yarrow Point","Skykomish","Milton","Preston","Snoqualmie Pass","Beaux Arts Village","Inglewood-Finn Hill"])



        output=""

        input_dict = {'bedrooms' : bedrooms, 'bathrooms' : bathrooms, 'sqft_living' : sqft_living, 'sqft_lot' : sqft_lot, 'floors' : floors, 'waterfront' : waterfront,
        'view':view,'condition':condition,'sqft_above':sqft_above,'sqft_basement':sqft_basement,'yr_built':yr_built,'yr_renovated':yr_renovated,'city':city}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
