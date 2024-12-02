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
    image=Image.open(r'data\me.jpeg')
    st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
        )

        "# Center an image when in fullscreen"
    "Images (and most elements in general) are always aligned to the left"
    
   
    st.image(image)


