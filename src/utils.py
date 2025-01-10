import functools
import logging

import streamlit as st
import yaml
from PIL import Image
import base64
from io import BytesIO


class CustomDict(dict):
    def __getitem__(self, key):
        for k in self.keys():
            if k.endswith(key):
                return super().__getitem__(k)
        raise KeyError(f"Key not found: {key}")


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


def set_png_as_page_bg(png_file, icon=False):
    bin_str = get_image_bin_file(png_file, icon=False)
    page_bg_img = f'''
    <style>
        .appview-container {{
            background-image: url("{bin_str}");
            background-repeat: repeat-y;
            background-size: cover; 
            background-position: top; 
        }}
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


with open('data/profile_data.yaml', 'r',errors='ignore') as file:
    profile = yaml.safe_load(file)
    career = CustomDict(profile['career'])
    education = CustomDict(profile['education'])
    certifications = CustomDict(profile['certifications'])
    skills = CustomDict(profile['skills'])
    contact_social = CustomDict(profile['contact_social'])


with open("src/frontend/custom_styles.css") as css:
    css_style = css.read()

with open('src/setup/config.yaml', 'r') as file:
    config = yaml.safe_load(file)


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


def container(*args, **kwargs):
    function = args[0]
    args = args[1:]
    if 'key' in kwargs:
        key = kwargs.pop('key')
        container = st.container(key=key)
        with container:
            return function(*args, **kwargs)

    return function(*args, **kwargs)

def del_seq(parm_text):
    if '.' in parm_text[1:2]: parm_text = parm_text.split('.',1)[1]
    return parm_text

def disp_icon_text(parm_key, text=None, link_flag=True, dict =contact_social):
    icon = dict[parm_key]['icon']

    if text is None:
        text = dict[parm_key]['name']

    if 'http' not in icon:
        icon = get_image_bin_file(icon)

    if link_flag:
        link = dict[parm_key]['link']
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
        container(disp_icon_text, 'ramana_portal', key='ramana_portal')
    width_weights_social = [1, .05, 1, 0.05, 1, .05, 1]
    linkedin_col, _, github_col, _, medium_col, _, _ = st.columns(width_weights_social,
                                                                  vertical_alignment='center')
    with linkedin_col:
        container(disp_icon_text, 'linkedin', key='social_linkedin')
    with github_col:
        container(disp_icon_text, 'github', key='social_contact')
    with medium_col:
        container(disp_icon_text, 'medium', key='social_medium')


def ruler():
    st.markdown("---")
