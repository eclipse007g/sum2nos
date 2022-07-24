import streamlit as st

st.write("""
# Sum of 2 Nos

This does sum of 2 nos
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_num = st.number_input("first no")
    second_num = st.number_input("second no")

    return first_num+second_num

total= user_input_features()

st.subheader('Sum')
st.write(total)
