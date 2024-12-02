import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Yogita Bhagtani",layout="wide")

st.markdown(
    """
    <h3 style='text-align:center;'>Yogita Bhagtani<h3>
    """,
    unsafe_allow_html=True)

selected=option_menu(
    menu_title=None,
    options=["Home","Skills","Qualifications"],
    icons=["house","book","envelope"],
    menu_icon="cast",
    default_index=0,
)

if selected=="Home":
    image=Image.open(r'data/me.jpeg')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(image)
    
   
    


