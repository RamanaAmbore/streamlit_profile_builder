import streamlit as st

import src.components
from src.utils import get_image_bin_file, del_seq, config, profile


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


def markdown(text, style_tag=True):
    if style_tag:
        text = f'<style>{text}</style>'

    st.markdown(f'{text}', unsafe_allow_html=True)


def container(*args, **kwargs):
    function = args[0]
    args = args[1:]
    if 'key' in kwargs:
        key = kwargs.pop('key')
        container = st.container(key=key)
        with container:
            return function(*args, **kwargs)

    return function(*args, **kwargs)


def write_section_heading(text, key=None, first_line=True, last_line=True):
    if first_line:
        create_ruler()
    icon = config["section_icons"]
    container(st.subheader, f':{icon[text]}: {text.title()}', key=key)
    if last_line:
        create_ruler()


def write_subheading(heading, text, key=None):
    st.write(f"**{heading.title()}:** {text}")


def disp_icon_text(icon=None, text="", link="#", tag=""):
    icon = get_image_bin_file(icon)
    if tag == "":
        tag = f"<img src='{icon}' class='href_icon'>{text}"
    else:
        tag = f"<{tag}><img src='{icon}' class='href_icon'>{text}</{tag}>"

    st.markdown(
        f"""
            <div class='icon_href_text_div'>
                <span> 
                    <a href="{link} " 
                    class='href_link'><span class='href_text'>{tag}</a>
                </span>
            </div>
            """,
        unsafe_allow_html=True
    )



def create_ruler():
    st.markdown('---', unsafe_allow_html=True)


def write_container(name):
    profile_section = profile[name]
    for key, vals in profile_section.items():
        disp_icon_text(vals['icon'], vals['long label'], vals['link'])


def write_colums(column_list, name):
    profile_section = profile[name]
    profile_keys = list(profile_section.keys())
    size = len(profile_keys) - 1
    profile_vals = list(profile_section.values())

    for idx, col in enumerate(column_list):
        if idx > size: return
        vals = profile_vals[idx]
        label = vals['label'] if 'label' in vals else profile_keys[idx]
        vals = profile_vals[idx]
        with col:
            disp_icon_text(vals['icon'], label, vals['link'])
