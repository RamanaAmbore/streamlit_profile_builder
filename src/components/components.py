import streamlit as st
from plotly import graph_objects as go
from streamlit_option_menu import option_menu

from src.utils import container, get_image_file, config, profile, get_image_bin_file, skills, write_subheading, ruler, \
    write_colums, contact, social, write_container, education
import plotly.graph_objects as go
import random


def generate_option_menu():
    with st.sidebar:
        selected = option_menu("", config['sections'],
                               icons=config['section_icons'], menu_icon="cast", default_index=-1,
                               styles={
                                   "container": {"padding": "0!important", "background-color": "#2c4653"},
                                   "icon": {"color": "white", "font-size": "20px", "fond-weight": "bold"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "color": "white",
                                                "margin": "0px",
                                                "--hover-color": "#616365"},
                                   "nav-link-selected": {"background-color": "#e6873a", "font-size": "15px"}}
                               )


def generate_summary_section():
    container(st.header, f'{profile['name']}, {profile['name_suffix']}', key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {profile['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        container(st.write, profile['summary'], key='summary')


def generate_skills_section():
    colors = config['colors']
    categories = [val['name'] for val in skills.values()]
    icon_paths = [val['icon'] for val in skills.values()]
    ratings = [val['level'] for val in skills.values()]
    select_colors = random.sample(colors, len(ratings))
    img_base64 = [get_image_bin_file(icon) for icon in icon_paths]

    write_subheading(':male-technologist: Skills', key='skills')

    # Create bar chart
    fig = go.Figure()

    # Add bars with categories inside (vertical text) and shadow around the bar
    for i, category in enumerate(categories):
        fig.add_trace(go.Bar(
            x=[category],
            y=[ratings[i]],
            text='',
            textposition='inside',
            insidetextanchor='start',
            marker=dict(color=select_colors[i], line=dict(color='#dfdfdf', width=1)),  # Light gray border with width 1
            name=category
        ))

        # Add vertical text inside the bars
        fig.add_annotation(
            x=category,
            y=1,  # Adjust position to start from bottom
            text=category,
            showarrow=False,
            textangle=-90,  # Vertical text
            yanchor='bottom',
            font=dict(color="#2f4550", size=14)
        )

        # Add images inside the bars just below the text

        fig.add_layout_image(
            dict(
                source=img_base64[i],
                x=i,
                y=0.1,
                xref='x',
                yref='y',
                sizex=.6,  # Larger icons
                sizey=.6,  # Larger icons
                xanchor='center',
                yanchor='bottom'
            ))

    # Update layout for transparent background and vertical x-axis labels
    fig.update_layout(
        xaxis_title=dict(text="Technical Skills", font=dict(color="#2f4550", size=14)),
        yaxis_title=dict(text="Skill Level", font=dict(color="#2f4550", size=14)),
        xaxis=dict(tickangle=0, showticklabels=False, ),  # Remove x-axis text by setting ticktext to an empty list),
        yaxis=dict(range=[0, 5]),
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
        margin=dict(t=20, b=20),
        showlegend=False
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


def generate_contact_social_section():
    ruler()
    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], contact)

    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], social)


def generate_education_section():
    global values
    write_subheading(':school: Education', key='school')
    width_education = [5, .05, 1]

    education_col, _, education_pie_chart_col = st.columns(width_education,
                                                           vertical_alignment='center')
    with education_col:
        write_container(education)

    with education_pie_chart_col:
        vals = education.values()
        labels = [i['short_name'] for i in vals]
        values = [i['duration'] for i in vals]
        select_colors = random.sample(config['colors'], len(labels))

        # Create pie chart
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color="gray", width=1)),
                   textinfo='label+percent', insidetextorientation='radial',
                   pull=[0.03] * len(labels))])

        # Update layout for custom appearance
        fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
