import logging

import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.logger import log_setup
from src.utils import get_profile_data, get_custom_css, get_config_data, markdown, get_image_file, disp_icon_text


def container(*args, **kwargs):
    function = args[0]
    args = args[1:]
    if 'key' in kwargs:
        key = kwargs.pop('key')
        container = st.container(key=key)
        with container:
            return function(*args, **kwargs)

    return function(*args, **kwargs)


if 'logger' not in st.session_state:
    st.session_state.logger = log_setup()
    logging.info('Logging setup')

if __name__ == '__main__':
    favicon = Image.open(get_image_file("ramana_photo_favicon.ico"))
    prof = get_profile_data()
    css_style = get_custom_css()
    config = get_config_data()

    st.set_page_config(page_title=f"{prof['name'].title()}'s Profile", page_icon=favicon, layout="wide")
    markdown(css_style)

    with st.sidebar:
        get_option_menu()
    st.header(f'{prof['name']}')
    # st.header(about_me_name)
    st.write(f'#### {prof['designation']}')
    col1, _, col2 = st.columns([1, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        st.write(prof['summary'])

    width_weights = [1.2, .05, 1.2, 0.05, 1.2, .05, 1.2]
    loc_col, _, mail_col, _, phone_col, _, _ = st.columns(width_weights, vertical_alignment='center')
    linkedin_col, _, github_col, _, medium_col, _, streamlit_col = st.columns(width_weights,
                                                                              vertical_alignment='center')
    with loc_col:
        container(disp_icon_text, 'loc', key='contact_loc')
    with mail_col:
        container(disp_icon_text, 'mail', key='contact_mail')
    with phone_col:
        container(disp_icon_text, 'phone', key='contact_phone')

    with linkedin_col:
        container(disp_icon_text, 'linkedin', key='social_linkedin')
    with github_col:
        container(disp_icon_text, 'github', key='social_contact')
    with medium_col:
        container(disp_icon_text, 'medium', key='social_medium')
    with streamlit_col:
        container(disp_icon_text, 'streamlit', key='social_streamlit')
