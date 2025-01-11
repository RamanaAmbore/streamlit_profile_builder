import logging

import numpy as np
import pandas as pd
from PIL import Image

from src.components.components import generate_option_menu, generate_summary_section, generate_skills_section, \
    generate_contact_social_section, generate_education_section
from src.logger import log_setup
from src.utils import css_style, profile, markdown, get_image_file, set_png_as_page_bg, milestones
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px


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

    # Generate example data
    np.random.seed(42)

    years = [2000, 2002, 2005, 2008, 2010, 2013, 2015, 2018, 2020, 2022]
    milestones = [f'Milestone {i}' for i in range(1, 11)]  # Example milestones
    impacts = np.random.randint(-100, 100, 10)  # Random impact values (positive and negative)
    categories = [f'Category {i}' for i in range(1, 11)]  # Categories for tooltip
    colors = np.random.rand(10)  # Random color values (normalized between 0 and 1)

    # Create a dataframe
    df = pd.DataFrame({
        'Year': years,
        'Milestone': milestones,
        'Impact': impacts,
        'Category': categories,
        'Color': colors
    })

    # Normalize the impact for vertical positioning
    df['Y'] = df['Impact'] / 10  # Scale down impact for Y position

    # Create the plotly figure
    fig = go.Figure()

    # Add shadow bubbles to simulate depth (more realistic effect)
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=[df['Year'][i] + 0.2],  # Offset shadow slightly to the right
            y=[df['Y'][i] - 0.6],  # Offset shadow slightly down for realistic depth
            mode='markers',
            marker=dict(
                size=abs(df['Impact'][i]) * 0.9,  # Shadow slightly smaller than bubble
                color='rgba(0, 0, 0, 0.3)',  # Semi-transparent black for shadow
                line=dict(width=0),  # No border for the shadow
                opacity=0.5,  # Slight opacity to create realistic depth
            ),
            hoverinfo='skip',  # No hover info for shadow
            showlegend=False  # Shadows do not appear in the legend
        ))

    # Add main bubbles
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=[df['Year'][i]],
            y=[df['Y'][i]],
            mode='markers+text',
            marker=dict(
                size=abs(df['Impact'][i]),  # Size proportional to the impact
                color=df['Color'],  # Use the pre-defined color from the dataframe
                opacity=0.9,  # Opacity for the bubbles
                line=dict(width=2, color='DarkSlateGrey'),  # Outline for the bubble
            ),
            text=df['Milestone'][i],
            textposition='top center',
            hovertemplate=(
                "<b>Year:</b> %{x}<br>"
                "<b>Impact:</b> %{y}<br>"
                "<b>Milestone:</b> %{text}<extra></extra>"
            ),
            showlegend=False  # Hide legend for now
        ))

    # Add vertical connecting lines from bubbles to the zero line (x-axis)
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=[df['Year'][i], df['Year'][i]],  # Same x value for both points
            y=[df['Y'][i], 0],  # From bubble position to zero line
            mode='lines',
            line=dict(
                color='black',  # Line color
                width=1,  # Line thickness
                dash='dot',  # Optional dotted line style for better visual appeal
            ),
            showlegend=False,  # No need for line to appear in the legend
            opacity=0.7,  # Make the line slightly transparent
            # Ensure the line is behind the bubble by setting a lower zindex
            legendgroup=str(i)  # Use this to keep traces grouped
            # Keep the line layer below bubbles
        ))

    # Add year annotations on the zero line (x-axis) in vertical upward direction
    for i, year in enumerate(df['Year']):
        fig.add_annotation(
            x=year,  # Position on the x-axis
            y=0,  # Position on the y-axis (on the zero line)
            text=str(year),  # Text for the year
            showarrow=False,  # No arrow for the annotation
            font=dict(
                size=12,  # Font size
                color="black",  # Font color
            ),
            align="center",  # Align the text
            valign="middle",  # Vertical alignment
            yshift=15,  # Slightly shift text upwards from the zero line
            textangle=90,  # Rotate text 90 degrees to make it vertical
        )

    # Set layout and styling
    fig.update_layout(
        title="Career Milestones with Shadow Effect and Connecting Lines",
        xaxis=dict(
            title="Year",
            tickvals=[],  # Remove the year ticks
            showgrid=False,  # No grid lines
            zeroline=True,  # Show the zero line
            zerolinecolor="black",  # Zero line color
            zerolinewidth=2,  # Thickness of the zero line
            showline=False,  # Hide the x-axis line itself
            ticks="",  # Remove ticks
        ),
        yaxis=dict(
            title="Impact",
            showgrid=False,
            zeroline=False,  # Hide the Y-axis zero line
            showline=False,  # Hide the Y-axis line
            ticks="",  # Remove the ticks
            tickvals=[],  # No ticks on the Y-axis
            ticktext=[],  # No tick labels on the Y-axis
        ),
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        hovermode='closest',  # Tooltips on closest bubble
        margin=dict(l=40, r=40, t=40, b=40)  # Adjust margins for better spacing
    )

    # Display the plot with Streamlit
    st.plotly_chart(fig)

    generate_skills_section()

    generate_education_section()

    # for section in config['sections']:
    #     i = section.upper()
    #     ruler()
    #     container(st.header, i, key=i)
