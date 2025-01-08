import logging

import streamlit as st
from PIL import Image

from src.components.components import generate_option_menu, generate_summary
from src.logger import log_setup
from src.utils import prof, css_style, markdown, get_image_file, container, \
    set_png_as_page_bg, disp_icon_text


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    favicon = Image.open(get_image_file("rambo_favicon.ico"))

    st.set_page_config(page_title=f"{prof['name'].title()}, {prof['name_suffix']}'s Profile", page_icon=favicon,
                       layout="wide")
    markdown(css_style)
    set_png_as_page_bg('background1.png')


def contact_setup():
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


if __name__ == '__main__':
    initial_setup()

    generate_option_menu()

    generate_summary()

    contact_setup()
