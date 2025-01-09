import streamlit as st
from streamlit_option_menu import option_menu

from src.utils import container, get_image_file, contact_social, config, profile, get_image_bin_file
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


def generate_summary():
    container(st.header, f'{profile['name']}, {profile['name_suffix']}', key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {profile['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        container(st.image, get_image_file('ramana_photo.png', False), clamp=True,
                  use_container_width=True, key='bio_photo')
    with col2:
        container(st.write, profile['summary'], key='summary')


def generate_barchart(categories, ratings, icon_paths, colors=config['colors']):
    select_colors = random.sample(colors, len(ratings))
    img_base64 = [get_image_bin_file(icon) for icon in icon_paths]

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
            marker=dict(color=select_colors[i], line=dict(color='#cfcfcf', width=1)),  # Light gray border with width 1
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
