# Import necessary modules and components
import logging  # Module for logging events and messages

import streamlit as st  # Streamlit module for building the web app
from PIL import Image  # PIL module for image handling

# Import custom components and functions from the src directory
from src.components import set_png_as_page_bg, markdown  # Functions for setting background and styling
from src.logger import log_setup  # Custom logging setup
from src.sections import generate_profile_section, generate_skills_section, \
    generate_education_section, generate_sidebar_section, \
    generate_certification_section, generate_employment_section, \
    generate_experience_summary_section, \
    generate_hobbie_section, generate_portfolio_section, \
    generate_project_section  # Functions to generate sections of the profile page
from src.utils import css_style, profile, \
    get_path  # Utility functions for styling, accessing profile data, and image paths


# Define the initial setup function to configure the Streamlit app
def initial_setup():
    # Initialize the logger in the session state if not already present
    if 'logger' not in st.session_state:
        st.session_state.logger = log_setup()  # Set up the logger
        logging.info('Logging setup')  # Log an informational message

    # Load the favicon image from the specified file path
    favicon = Image.open(get_path("rambo_favicon.ico"))

    # Set the page configuration for the Streamlit app
    st.set_page_config(
        page_title=f"{profile['name'].title()}, {profile['name suffix']}'s Profile",  # Set the page title dynamically
        page_icon=favicon,  # Use the favicon image
        layout="wide"  # Use a wide layout for the app
    )

    # Apply CSS styling to the page content
    markdown(css_style)

    # Set the background image for the page
    set_png_as_page_bg('background.png')


# Main function to execute the initial setup and generate different sections of the profile page
if __name__ == '__main__':
    initial_setup()  # Call the setup function to configure the app

    # Generate the sidebar section
    generate_sidebar_section()

    # Generate the profile section
    generate_profile_section()

    # Generate the experience summary section
    generate_experience_summary_section()

    # Generate the skills section
    generate_skills_section()

    # Generate the employment section
    generate_employment_section()

    # Generate the project section
    generate_project_section()

    # Generate the portfolio section
    generate_portfolio_section()

    # Generate the education section
    generate_education_section()

    # Generate the certification section
    generate_certification_section()

    # Generate the hobbies section
    generate_hobbie_section()
