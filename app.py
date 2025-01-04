import streamlit as st
from PIL import Image

from src.components.option_component import get_option_menu
from src.utils import get_profile_data, get_custom_css, get_config_data, markdown

import functools


def func(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        st.markdown(f'<div class="{args[0]}"></div>', unsafe_allow_html=True)
        # st.write(f"Executing {func.__name__} with args: {args} and kwargs: {kwargs}...")
        args = args[1:]
        result = function(*args, **kwargs)
        # st.write(f"Finished executing {func.__name__}.")
        return result

    return wrapper


if __name__ == '__main__':
    favicon = Image.open("assets/images/favicon.ico")
    prof = get_profile_data()
    css_style = get_custom_css()
    config = get_config_data()

    st.set_page_config(page_title=f"{prof['name'].title()}'s Profile", page_icon=favicon, layout="wide")
    markdown(css_style)

    with st.sidebar:
        get_option_menu()

    col1, _, col2 = st.columns([3, .1, 10])
    with col1:
        func(st.image)('bio_photo', 'assets/images/ramana_photo5.png', clamp=True, use_container_width=True)
    with col2:
        st.header(f'{prof['name']}')
        # st.header(about_me_name)
        st.write(f'#### {prof['designation']}')
        st.write(prof['summary'])
        _, contact_icon1, _, contact_text1, _, contact_icon2, _, contact_text2 = st.columns(
            [2, 1, .005, 3, .2, 1, .005, 5])
        with contact_icon1:
            st.image(config['phone_icon'], width=50, clamp=True)
        with contact_text1:
            func(st.write)('phone_icon', "##### (XXX) XXX-XXXX")
        with contact_icon2:
            st.image(config['mail_icon'], width=50, clamp=True)
        with contact_text2:
            func(st.write)('contact_icon', "##### Ramana.Ambore@gmail.com")
        _, linkedin_icon1, _, linkedin_link1, _, github_icon2, _, github_link2, _, medium_icon3, _, medium_link3 = st.columns(
            [.2, 1, .005, 3,
             .2, 1, .005, 5,
             .2, 1, .005, 5
             ])
        with linkedin_icon1:
            st.image(config['linkedin_icon'], width=50, clamp=True)
        with linkedin_link1:
            func(st.write)('phone_icon', "##### test")
        with github_icon2:
            st.image(config['github_icon'], width=50, clamp=True)
        with github_link2:
            func(st.write)('contact_icon', "##### test")
        with medium_icon3:
            st.image(config['medium_icon'], width=50, clamp=True)
        with medium_link3:
            func(st.write)('contact_icon', "##### test")
