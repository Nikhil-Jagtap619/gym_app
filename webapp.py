# if you.copy(my_code):
#   me.haunt(you)
import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
model = pickle.load(open("rf_trained_model.sav","rb")) #loading the created model


st.set_page_config(page_title="GYM Application") #tab title

#prediction function
def predict_status(age, height, weight):
    input_data = np.asarray([age, height, weight])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction

def main():

    # titling your page
    st.title("Fitness Prediction App")
    st.write("A quick Machine Learning model that predicts the health status based on the given dataset")

    #getting the input
    age = st.text_input("Enter your Age")
    height = st.text_input("Enter your Height in Feet")
    weight = st.text_input("Enter your Weight in Pounds")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
        diagnosis = predict_status(age, height, weight)
        if diagnosis=="Underweight":
            st.info("You're Under Weight")
            st.markdown("![You're like this!](https://i.gifer.com/L6m.gif)")
        elif diagnosis=="Healthy":
            st.success("You're Healthy")
            st.markdown("![keep up your health dude!](https://i.gifer.com/lf.gif)")
        elif diagnosis=="Overweight":
            st.warning("You're Over Weight")
            st.markdown("![Go Excercise!](https://i.gifer.com/8TK.gif)")
        else:
            st.error("Obesity!")
            st.markdown("![You need HELP!](https://i.gifer.com/5Waz.gif)")
        st.subheader("what next? Take Action Towards Better Health")
        st.write("🙋🏼‍♂️ Maintaining a healthy weight is important for your heart health")
        st.write("🙋🏼‍♂️ Don't be like Spongebob or Patrik")
        st.write("Maintain a Healthy Weight: [ check right now!](https://www.nhlbi.nih.gov/heart-truth/maintain-a-healthy-weight)")
        st.info("My Review")
        txt2 = "🔹 I had to refill the incorrect BMI values in order to have the correct class"
        txt3 = "🔹 Highly unbalanced target column"
        txt4 = "🔹 Random_Forest showed better results than any other algorithm i tired"
        for j in [txt2,txt3,txt4]:
            st.write(j)

        st.write("## Thank you for Visiting \nProject by Nikhil J")
        st.markdown("<h1 style='text-align: right; color: blue; font-size: small;'><a href='https://github.com/Nikhil-Jagtap619/gym_app'>Looking for Source Code?</a></h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)

    


if __name__=="__main__":
    main()


