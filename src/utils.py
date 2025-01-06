import functools
import logging

import streamlit as st
import yaml
from PIL import Image
import base64
from io import BytesIO

from tornado.httputil import format_timestamp


def get_image_bin_file(file, icon=True):
    # with open(bin_file, 'rb') as f:
    #     data = f.read()
    # return base64.b64encode(data).decode()
    # Open the image file
    img = Image.open(get_image_file(file, icon))
    format = file[-3:].upper()

    # Encode the image as base64
    buffered = BytesIO()
    img.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    url = f'data:image/{format.lower()};base64,{img_str}'
    return url


def set_png_as_page_bg(png_file):
    bin_str = get_image_bin_file(png_file)
    page_bg_img = '''
    <style>
        .appview-container {
        background-image: url("data:image/png;base64,%s");
        position: absolute; 
        background-repeat: no-repeat;
        background-size: cover;
        top: 0; 
        left: 0; }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


def get_profile_data():
    with open('data/profile_data.yaml', 'r') as file:
        return yaml.safe_load(file)


def get_custom_css():
    with open("src/frontend/custom_styles.css") as css:
        return css.read()


def get_config_data():
    with open('src/setup/config.yaml', 'r') as file:
        return yaml.safe_load(file)


def markdown(text, style_tag=True):
    if style_tag:
        text = f'<style>{text}</style>'

    st.markdown(f'{text}', unsafe_allow_html=True)


def debug_wrapper(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logging.debug(f'{function.__name__} started')
        result = function(*args, **kwargs)
        # st.write(f"Finished executing {func.__name__}.")
        logging.debug(f'{function.__name__} ended')
        return result

    return wrapper


def get_image_file(file, icon=True):
    if icon:
        return f'static/icons/{file}'
    else:
        return f'static/images/{file}'
