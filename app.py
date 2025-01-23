import logging

import streamlit as st
from PIL import Image

from src.components.components import set_png_as_page_bg, markdown
from src.components.sections import generate_profile_section, generate_skills_section, \
    generate_contact_social_section, generate_education_section, generate_sidebar_section, \
    generate_certification_section, generate_employment_section, \
    generate_experience_summary_section, \
    generate_hobbie_section, generate_portfolio_section, generate_project_section
from src.logger import log_setup
from src.utils import css_style, profile, get_image_path


def initial_setup():
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    favicon = Image.open(get_image_path("rambo_favicon.ico"))

    st.set_page_config(
        page_title=f"{profile['name'].title()}, {profile['name suffix']}'s Profile",
        page_icon=favicon,
        layout="wide")
    markdown(css_style)
    set_png_as_page_bg('background.png')


if __name__ == '__main__':
    initial_setup()

    generate_sidebar_section()

    generate_profile_section()

    generate_contact_social_section()

    generate_experience_summary_section()

    generate_skills_section()

    generate_employment_section()

    generate_project_section()

    generate_portfolio_section()

    generate_education_section()

    generate_certification_section()

    generate_hobbie_section()
