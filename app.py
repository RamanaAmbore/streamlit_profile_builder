import logging

import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.logger import log_setup
from src.utils import get_profile_data, get_custom_css, get_config_data, markdown, get_image_file, container, \
    set_png_as_page_bg, disp_icon_text


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')


if __name__ == '__main__':
    initial_setup()
    favicon = Image.open(get_image_file("rambo_favicon.ico"))
    prof = get_profile_data()
    css_style = get_custom_css()
    config = get_config_data()

    st.set_page_config(page_title=f"{prof['name'].title()}, {prof['name_suffix']}'s Profile", page_icon=favicon,
                       layout="wide")
    markdown(css_style)
    set_png_as_page_bg('Rx.png')

    with st.sidebar:
        get_option_menu()
    container(st.header, f'{prof['name']}, {prof['name_suffix']}', key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {prof['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        container(st.write, prof['summary'], key='summary')

    width_weights_contact = [1, .05, 1, 0.05, 1, .05, 1]
    mail_col, _, phone_col, _, loc_col, _, streamlit_col = st.columns(width_weights_contact,
                                                                      vertical_alignment='center')
    with loc_col:
        container(disp_icon_text, 'loc', key='contact_loc')
    with mail_col:
        container(disp_icon_text, 'mail', key='contact_mail')
    with phone_col:
        container(disp_icon_text, 'phone', key='contact_phone')
    with streamlit_col:
        container(disp_icon_text, 'streamlit', key='social_streamlit')

    width_weights_social = [1, .05, 1, 0.05, 1, .05, 1]
    linkedin_col, _, github_col, _, medium_col, _, _ = st.columns(width_weights_social,
                                                                  vertical_alignment='center')

    with linkedin_col:
        container(disp_icon_text, 'linkedin', key='social_linkedin')
    with github_col:
        container(disp_icon_text, 'github', key='social_contact')
    with medium_col:
        container(disp_icon_text, 'medium', key='social_medium')
