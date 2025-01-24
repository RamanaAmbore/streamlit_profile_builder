# Import necessary modules and components
import logging

import streamlit
import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

# Import custom components and functions from src directory
from src.components import set_png_as_page_bg, markdown
from src.sections import generate_profile_section, generate_skills_section, \
    generate_contact_social_section, generate_education_section, generate_sidebar_section, \
    generate_certification_section, generate_employment_section, \
    generate_experience_summary_section, \
    generate_hobbie_section, generate_portfolio_section, generate_project_section
from src.logger import log_setup
from src.utils import css_style, profile, get_image_path

# Define the initial setup function to configure the Streamlit app
def initial_setup():
    # Initialize the logger in session state if not already present
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()
        logging.info('Logging setup')

    # Load the favicon image
    favicon = Image.open(get_image_path("rambo_favicon.ico"))

    # Set the page configuration for the Streamlit app
    st.set_page_config(
        page_title=f"{profile['name'].title()}, {profile['name suffix']}'s Profile",
        page_icon=favicon,
        layout="wide"
    )

    # Apply CSS styling to the markdown
    markdown(css_style)

    # Set the background image for the page
    set_png_as_page_bg('background.png')

# Main function to execute the initial setup and generate different sections of the profile page
if __name__ == '__main__':
    initial_setup()

    # Add JavaScript for smooth scrolling with debugging
    # Add JavaScript for scrolling
    st.markdown(
        """
        <script>
        function scrollTo(sectionId) {
            console.log("Scrolling to:", sectionId); // Debug log
            const element = document.getElementById(sectionId);
            if (element) {
                console.log("Found element:", element);
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                console.error("Element not found for section ID:", sectionId);
            }
        }
        </script>
        """,
        unsafe_allow_html=True,
    )

    selected = generate_sidebar_section()

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

    st.markdown(f"<script>scrollTo('{selected}');</script>", unsafe_allow_html=True)
