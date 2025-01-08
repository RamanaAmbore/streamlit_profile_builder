import logging

import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.logger import log_setup
from src.utils import get_profile_data, get_custom_css, get_config_data, markdown, get_image_file, container, \
    get_image_bin_file, set_png_as_page_bg


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')


def disp_icon_text(parm_text, link_flag=True):
    icon = prof[f'{parm_text}_icon']
    text = prof[f'{parm_text}_text']

    if 'http' not in icon:
        icon = get_image_bin_file(icon)

    if link_flag:
        link = prof[f'{parm_text}_link']
        st.markdown(
            f"""
            <div class='icon_href_text_div'>
                <span> <a href="{link}" class='href_link'><span class='href_text'><img src='{icon}' class='href_icon'>{text}</span></a></span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class='icon_text_div'>
                <img src='{icon}' class='no_href_icon'>
                <span class='no_href_text'> {text} </span>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == '__main__':
    initial_setup()
    favicon = Image.open(get_image_file("rambo_favicon.ico"))
    prof = get_profile_data()
    css_style = get_custom_css()
    config = get_config_data()

    st.set_page_config(page_title=f"{prof['name'].title()}, {prof['name_suffix']}'s Profile", page_icon=favicon, layout="centered")
    markdown(css_style)
    set_png_as_page_bg('R2.png')

    with st.sidebar:
        get_option_menu()
    container(st.header, f'{prof['name']}, {prof['name_suffix']}' , key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {prof['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2.5, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        st.write(prof['summary'])
        width_weights_contact = [1, .05, 1, 0.05, 1]
        loc_col, _, mail_col, _, phone_col = st.columns(width_weights_contact, vertical_alignment='center')
        with loc_col:
            container(disp_icon_text, 'loc', key='contact_loc')
        with mail_col:
            container(disp_icon_text, 'mail', key='contact_mail')
        with phone_col:
            container(disp_icon_text, 'phone', key='contact_phone')


    width_weights_social = [.05, 0.72, .05, 1, 0.05, 1, .05,1]


    _, streamlit_col, _, github_col,_,medium_col, _, linkedin_col = st.columns(width_weights_social, vertical_alignment='center')



    with streamlit_col:
        container(disp_icon_text, 'streamlit', key='social_streamlit')
    with linkedin_col:
        container(disp_icon_text, 'linkedin', key='social_linkedin')
    with github_col:
        container(disp_icon_text, 'github', key='social_contact')
    with medium_col:
        container(disp_icon_text, 'medium', key='social_medium')
