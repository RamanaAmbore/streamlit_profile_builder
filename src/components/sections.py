import numpy as np
import pandas as pd
import streamlit as st
from plotly import graph_objects as go
from streamlit_option_menu import option_menu

from src.components.components import container, write_subheading, create_ruler, write_colums, write_container
from src.utils import profile, get_image_path, get_sample, colors, get_image_bin_file, freq_color, contact, \
    social, education, config, get_config, get_profile, colors, dark_colors


def generate_sidebar_section():
    key_list, val_list = get_config('sidebar_icons')
    key_list = [ x.title() for x in key_list]
    with st.sidebar:
        selected = option_menu("", key_list,
                               icons=val_list, menu_icon="cast", default_index=-1,
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
        container(st.image, get_image_path('profile_photo.png', False), clamp=True,
                  use_container_width=True, key='profile_photo')
    with col2:
        container(st.write, profile['summary'], key='summary')


def generate_contact_social_section():
    create_ruler()
    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], 'contact')

    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], 'social')


def generate_skills_section():
    section_name = 'skills'
    key_list, val_list = get_profile(section_name)

    write_subheading(section_name, key=section_name)

    categories = [val['name'] for val in val_list]
    icon_paths = [val['icon'] for val in val_list]
    ratings = [val['level'] for val in val_list]
    select_colors = get_sample(colors, len(ratings))

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
            marker=dict(
                color=select_colors[i],  # Base color
                line=dict(color='lightgray', width=1)  # Shadow effect with darker border
            ),
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
            font=dict(color=freq_color, size=14)
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
        xaxis_title=dict(text="Technical Skills", font=dict(color=freq_color, size=14)),
        yaxis_title=dict(text="Skill Level", font=dict(color=freq_color, size=14)),
        xaxis=dict(tickangle=0, showticklabels=False, ),
        yaxis=dict(range=[0, 5]),
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
        margin=dict(t=20, b=20),
        showlegend=False
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


def generate_education_section():
    section_name = 'education'
    key_list, val_list = get_profile(section_name)
    write_subheading(section_name, key=section_name)

    width_education = [5, .05, 1]

    education_col, _, education_pie_chart_col = container(st.columns, width_education,
                                                          vertical_alignment='center', key='education_container')
    with education_col:
        write_container('education')

    with education_pie_chart_col:
        vals = education.values()
        labels = [val['name'] for val in val_list]
        values = [val['duration'] for val in val_list]
        select_colors = get_sample(colors, len(labels))

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
            margin=dict(t=0, b=0),
            height=150
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

def generate_certification_section():
    section_name = 'certifications'
    key_list, val_list = get_profile(section_name)
    write_subheading(section_name, key=section_name)

    width_education = [5, .05, 1]

    col, _, pie_chart_col = container(st.columns, width_education,
                                                          vertical_alignment='center', key='certification_container')
    with col:
        write_container('certifications')

    with pie_chart_col:
        labels = [val['name'] for val in val_list]
        values = [val['duration'] for val in val_list]
        select_colors = get_sample(colors, len(labels))

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
            margin=dict(t=0, b=0),
            height=150
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)


def generate_milestonre_section():
    # Generate example data
    create_ruler()
    section_name = 'milestones'
    key_list, val_list = get_profile(section_name)
    # write_subheading(section_name, key=section_name)

    years = key_list
    milestones = [i['name'] for i in val_list]  # Example milestones
    impacts = [i['impact'] *3 for i in val_list]   # Random impact values (positive and negative)
    hover = [i['hover'] for i in val_list]  # Categories for tooltip
    Y = [i['y'] for i in val_list]
    select_colors = get_sample(dark_colors, len(years))
    # Create a dataframe
    df = pd.DataFrame({
        'Y': Y,
        'X': years,
        'Milestone': milestones,
        'Impact': impacts ,
        'Hover': hover,
        'Color': select_colors
    })

    fig = go.Figure()

    # Add shadow effect as a larger, semi-transparent circle behind each bubble
    for _, row in df.iterrows():
        # Add shadow (slightly larger and semi-transparent)
        fig.add_trace(go.Scatter(
            x=[row['X']],
            y=[row['Y']],
            marker=dict(
                size=row['Impact'] * 1.2,  # Slightly larger for shadow
                color='rgba(50, 50, 50, 0.2)',  # Semi-transparent gray
            ),
            mode='markers',
            hoverinfo='skip',  # Hide shadow hover info
            showlegend=False  # Do not include in legend
        ))

        # Add main bubble
        fig.add_trace(go.Scatter(
            x=[row['X']],
            y=[row['Y']],
            marker=dict(
                size=row['Impact'],  # Bubble size based on 'Impact'
                color =row['Color'] ,
                line=dict(color='gray', width=1)  # Border for the bubble
            ),
            mode='markers+text',
            text=row['Milestone'],  # Display milestone inside or near the bubble
            textposition='top center',  # Position of the text
            hovertext=row['Hover'],  # Hover text from DataFrame
            hoverinfo='text',
            name=row['Milestone']  # Name for the legend (optional)
        ))

        # Add dotted line connecting bubble to x-axis
        fig.add_trace(go.Scatter(
            x=[row['X'], row['X']],
            y=[1, row['Y']*0.8],  # Connects bubble to x-axis
            mode='lines',
            line=dict(color=freq_color, width=1, dash='dash'),  # Dotted line
            hoverinfo='skip',  # No hover for the line
            showlegend=False  # Do not include in legend
        ))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            linecolor=freq_color,
            linewidth=1,
            showgrid=False,
            zeroline=False,
            tickvals=df['X'],  # Use only the years in the DataFrame for x-axis ticks
            ticktext=df['X'],  # Ensure the labels match the ticks
            type='category'  # Treat the x-axis as categorical (ordinal)
        ),
        yaxis=dict(
            showline=False,  # Hide y-axis line
            showgrid=False,  # Hide grid lines
            zeroline=False,  # Hide the zero line
            tickvals = [],
            ticktext = []
    ),
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
        showlegend=False,
        margin=dict(t=10, b=10),
        height=350
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)

