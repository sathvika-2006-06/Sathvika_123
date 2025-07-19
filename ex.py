import streamlit as st
st.title('Interactive User interface Example')

#Take text input
user_text=st.text_input('Enter some text')

#Add a slider
slider_value=st.slider('Select a number',0,100,50)

#Button interaction
if st.button('submit'):
    st.write(f'you entered:{user_text}')
    st.write(f'slider_value:{slider_value}')