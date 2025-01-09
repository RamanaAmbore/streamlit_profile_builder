import logging

import streamlit as st
from PIL import Image

from src.components.components import generate_option_menu, generate_summary, generate_barchart
from src.logger import log_setup
from src.utils import contact_social, css_style, profile, config, markdown, get_image_file, set_png_as_page_bg, \
    contact_setup, container, \
    ruler, skills

import streamlit as st
import plotly.graph_objects as go


def career_glance():
    pass


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    favicon = Image.open(get_image_file("rambo_favicon.ico"))

    st.set_page_config(page_title=f"{profile['name'].title()}, {profile['name_suffix']}'s Profile", page_icon=favicon,
                       layout="wide")
    markdown(css_style)
    set_png_as_page_bg('background.png')


if __name__ == '__main__':
    initial_setup()

    generate_option_menu()

    generate_summary()
    ruler()
    contact_setup()

    ruler()

    container(st.subheader,'Skills',key='skills')
    categories = [val['name'] for val in skills.values()]
    icons = [val['icon'] for val in skills.values()]
    ratings = [val['level'] for val in skills.values()]
    generate_barchart(categories, ratings, icons)

    ruler()
    # for section in config['sections']:
    #     i = section.upper()
    #     ruler()
    #     container(st.header, i, key=i)
