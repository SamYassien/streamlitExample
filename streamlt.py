import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += 1

def decrement_counter(decrement_value=0):
    st.session_state.count -= 1

st.button('Increment', on_click=increment_counter)

st.button('Decrement', on_click=decrement_counter)

st.write('Count = ', st.session_state.count)