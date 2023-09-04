#!/usr/bin/env python
# coding: utf-8

# In[45]:


import streamlit as st
import tensorflow as tf

# Load your model here
loaded_model = tf.saved_model.load("model_0_SaveModel_format")

# Customize Streamlit app appearance
st.markdown(
    '''
    <style>
    body {
        background-image: url("https://www.crowdstrike.com/wp-content/uploads/2020/11/Blog_1060x698-25-1.jpg");
        background-size: cover;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)


# Title
st.title("Terror Attack Prediction")

# Define dropdown options for each feature
attack_type_options = ["Bombing","Kidnapping", "Shooting", "Hijacking", "Arson", "Assasination"]

location_options = ['Athens','Bankok','Beijing','Berlin','Buenos','Cape','Dubai','Istanbul',
                    'Jakarta','Lima','London','Madrid','Mexico','Moscow','New','Paris','Rome',
                    'Seoul','Sydney','Tokyo']

perpetrator_options = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G',
                       'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N', 
                       'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T', 'Group U', 
                       'Group V', 'Group W', 'Group X', 'Group Y', 'Group Z']


weapon_used_options = ["Explosives","Bladed Weapons" "Firearms", "Chemicals","Meele"]

claimed_by_options = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G',
                      'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N',
                      'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T', 'Group U', 
                      'Group V', 'Group W', 'Group X', 'Group Y', 'Group Z']


# Create dropdowns for each feature
input1 = st.selectbox("Attack_Type:", attack_type_options)
input2 = st.selectbox("Location:", location_options)
input3 = st.selectbox("Perpetrator:", perpetrator_options)
input4 = st.selectbox("Weapon_Used:", weapon_used_options)
input5 = st.selectbox("Claimed_by:", claimed_by_options)

# Numeric input for Victims_Injured and Victims_Deceased
input6 = st.number_input("Victims_Injured:", min_value=0)
input7 = st.number_input("Victims_Deceased:", min_value=0)

# Check if Victims_Injured and Victims_Deceased are provided
if input6 > 0 or input7 > 0:
    to_predict = [f'{input1} in {input2} by {input3} with {input4} claimed by {input5}. {int(input6)} are injured and {int(input7)} are deceased']

    # Create a TensorFlow constant with the input data
    input_data = tf.constant(to_predict, dtype=tf.string)

    # Add a Button for Prediction:
    if st.button("Predict"):
        # Perform predictions using your model or algorithm
        prediction = loaded_model([input_data])

#         prediction = loaded_model(input_data)

        # Determine the prediction result
        if tf.round(prediction):
            prediction = 'Major Attack'
        else:
            prediction = 'Minor Attack'

        # Display the prediction result
        st.write("Prediction:", prediction)


# In[43]:


# x=['Shooting in Dubai by Group C with Bladed Weapons claimed by Group D. 5 are injured and 19 are deceased']
# x = tf.constant(x, dtype=tf.string)
# loaded_model([x])


# In[ ]:




