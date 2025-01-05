import logging

import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.logger import log_setup
from src.utils import get_profile_data, get_custom_css, get_config_data, markdown, get_image_file


def container(*args, **kwargs):
    function = args[0]
    args = args[1:]
    if 'key' in kwargs:
        key = kwargs.pop('key')
        container = st.container(key=key)
        with container:
            return function(*args, **kwargs)

    return function(*args, **kwargs)

def disp_icon_text(icon_link, text):
    st.markdown(
        f"""
        <div style='display: flex; align-items: center; font-weight: bold; font-size: 20; padding:0rem;'>
            <img src='{config[icon_link]}' style='width: 30px; margin-right: 10px;'>
            <span> {text} </span>
        </div>
        """,
        unsafe_allow_html=True
    )

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

    col1, _, col2 = st.columns([3, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        st.header(f'{prof['name']}')
        # st.header(about_me_name)
        st.write(f'#### {prof['designation']}')
        st.write(prof['summary'])

        loc_col, _, mail_col, _, phone_col = st.columns([0.7, .05, 1, .05, 1],vertical_alignment='center')
        with loc_col:
            disp_icon_text('loc_icon', 'Des Moines, Iowa')
        with mail_col:
            disp_icon_text('phone_icon', 'Ramana.Ambore@gmail.com')
        with phone_col:
            disp_icon_text('mail_icon', '(XXX) XXX-XXXX')

    linkedin_col, _, github_col = st.columns([ 1, .05, 2],vertical_alignment='center')
    with linkedin_col:
        disp_icon_text('linkedin_icon', config['linkedin'])
    with github_col:
        disp_icon_text('github_icon', config['github'])

    medium_col, _, streamlit_col = st.columns([ 1, .05, 2],vertical_alignment='center')
    with medium_col:
        disp_icon_text('medium_icon', config['medium'])
    with streamlit_col:
        disp_icon_text('streamlit_icon', config['streamlit'])
        # linkedin_icon1_, github_icon2, _, github_link2, _, medium_icon3, _, medium_link3 = st.columns(
        #     [.2, 1, .005, 3,
        #      .2, 1, .005, 5,
        #      .2, 1, .005, 5
        #      ])
        # with linkedin_icon1:
        #     st.image(config['linkedin_icon'], width=50, clamp=True)
        # with linkedin_link1:
        #     container(st.write)('phone_icon', "##### test")
        # with github_icon2:
        #     st.image(config['github_icon'], width=50, clamp=True)
        # with github_link2:
        #     container(st.write)('contact_icon', "##### test")
        # with medium_icon3:
        #     st.image(config['medium_icon'], width=50, clamp=True)
        # with medium_link3:
        #     container(st.write)('contact_icon', "##### test")
