import logging

from PIL import Image

from src.components.components import generate_option_menu, generate_summary_section, generate_skills_section, \
    generate_contact_social_section, generate_education_section
from src.logger import log_setup
from src.utils import css_style, profile, markdown, get_image_file, set_png_as_page_bg

import streamlit as st


def career_glance():
    pass


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    favicon = Image.open(get_image_file("rambo_favicon.ico"))

    st.set_page_config(
        page_title=f"{profile['name'].title()}, {profile['name_suffix']}'s Profile",
        page_icon=favicon,
        layout="wide")
    markdown(css_style)
    set_png_as_page_bg('background.png')


if __name__ == '__main__':
    initial_setup()
    generate_option_menu()

    generate_summary_section()

    generate_contact_social_section()

    generate_skills_section()

    generate_education_section()

    # for section in config['sections']:
    #     i = section.upper()
    #     ruler()
    #     container(st.header, i, key=i)
