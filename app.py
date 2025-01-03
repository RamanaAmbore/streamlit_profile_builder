import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.utils import load_profile_data, load_css

if __name__ == '__main__':
    favicon = Image.open("assets/images/favicon.ico")
    prof = load_profile_data()
    css_style = load_css()

    st.set_page_config(page_title="Ramana Ambore(Rambo)'s Profile", page_icon=favicon, layout="wide")
    st.markdown(css_style, unsafe_allow_html=True)

    with st.sidebar:
        get_option_menu()

    col1, div, col2 = st.columns([1.5, .1, 10])
    with col1:
        st.image('assets/images/ramana_photo1.png', clamp=True, use_container_width=True)
    with col2:
        st.header(f'{prof['name']}')
        # st.header(about_me_name)
        st.markdown(
            f'<h4 style="color:#f87408;font-weight:bold;padding-top:0rem;letter-spacing:0px">{prof['designation']}</h4>',
            unsafe_allow_html=True)
        st.write(prof['summary'])
