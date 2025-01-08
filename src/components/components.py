import streamlit as st
from streamlit_option_menu import option_menu

from src.utils import container, get_image_file, prof, config


def generate_option_menu():
    with st.sidebar:
        selected = option_menu("", config['sections'],
                               icons=config['section_icons'], menu_icon="cast", default_index=-1,
                               styles={
                                   "container": {"padding": "0!important", "background-color": "#2c4653"},
                                   "icon": {"color": "white", "font-size": "20px", "fond-weight": "bold"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "color": "white",
                                                "margin": "0px",
                                                "--hover-color": "#616365"},
                                   "nav-link-selected": {"background-color": "#e6873a", "font-size": "15px"}}
                               )


def generate_summary():
    container(st.header, f'{prof['name']}, {prof['name_suffix']}', key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {prof['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        container(st.write, prof['summary'], key='summary')
