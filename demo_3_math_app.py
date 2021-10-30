import streamlit as st
# https://docs.streamlit.io/library/api-reference/widgets

X = st.number_input("X", step=1)
Y = st.select_slider("Y", range(0, 10))

show_balloons = st.checkbox("Show balloons?")
if st.button("Add"):
    st.write(f" Your answer is {X + Y}")
    if show_balloons:
        st.balloons()
