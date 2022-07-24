import streamlit as st

st.write("""
# Sum of 2 Nos

This does sum of 2 nos
""")
#Get Input

st.header('User Input Parameters')

first_num = st.number_input("first no")
second_num = st.number_input("second no")

total=first_num+second_num

st.subheader('Sum')
st.write(total)
