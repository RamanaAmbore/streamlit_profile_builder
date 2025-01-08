import logging

import streamlit as st
from PIL import Image

from src.components.components import generate_option_menu, generate_summary
from src.logger import log_setup
from src.utils import prof, css_style, config, markdown, get_image_file, set_png_as_page_bg, contact_setup, container, \
    ruler


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    favicon = Image.open(get_image_file("rambo_favicon.ico"))

    st.set_page_config(page_title=f"{prof['name'].title()}, {prof['name_suffix']}'s Profile", page_icon=favicon,
                       layout="wide")
    markdown(css_style)
    set_png_as_page_bg('background.png')


if __name__ == '__main__':
    initial_setup()

    generate_option_menu()

    generate_summary()
    ruler()
    contact_setup()


    for section in config['sections']:
        i = section.upper()
        ruler()
        container(st.header, i,  key=i)
