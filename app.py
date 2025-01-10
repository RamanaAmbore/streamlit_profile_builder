import logging
import random

import streamlit as st
from PIL import Image

from src.components.components import generate_option_menu, generate_summary, generate_barchart
from src.logger import log_setup
from src.utils import contact_social, css_style, profile, config, markdown, get_image_file, set_png_as_page_bg, \
    contact_setup, container, \
    ruler, skills, disp_icon_text, education

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

    container(st.subheader,':male-technologist: Skills',key='skills')
    ruler()
    categories = [val['name'] for val in skills.values()]
    icons = [val['icon'] for val in skills.values()]
    ratings = [val['level'] for val in skills.values()]
    generate_barchart(categories, ratings, icons)

    ruler()
    container(st.subheader,':school: Education',key='education')
    ruler()


    width_education = [3, .05, 1]
    education_col, _, education_pie_chart_col = st.columns(width_education,
                                                                      vertical_alignment='center')
    with education_col:
            container(disp_icon_text, 'msc', key='edu_msc',dict = education)
            container(disp_icon_text, 'pgdbm', key='edu_pgdbm',dict = education)
            container(disp_icon_text, 'bsc', key='edu_bsc',dict = education)

    with education_pie_chart_col:
        # Sample data
        labels = [i['name'] for i in education.values()]
        values = [i['duration'] for i in education.values()]
        select_colors = random.sample(config['colors'], len(labels))

        # Create pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict( colors=select_colors, line=dict(color="gray", width=1) ),
                                     textinfo='label+percent', insidetextorientation='radial',pull=[0.03] * len(labels))])

        # Update layout for custom appearance
        fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
            showlegend=False,
            margin=dict(t=20, b=20),
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig)

    # for section in config['sections']:
    #     i = section.upper()
    #     ruler()
    #     container(st.header, i, key=i)
