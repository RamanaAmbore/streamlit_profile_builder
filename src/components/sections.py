import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from plotly import graph_objects as go
from streamlit_option_menu import option_menu
import plotly.express as px
import base64

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

def generate_employment_section():
    section_name = 'employment'
    key_list, val_list = get_profile(section_name)
    write_subheading(section_name, key=section_name)

    width_education = [5, .05, 1]

    col, _, pie_chart_col = container(st.columns, width_education,
                                                          vertical_alignment='center', key='employment_container')
    with col:
        write_container('employment')

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


def generate_milestone_section():
    section = profile['milestones']
    df = pd.DataFrame.from_dict(section, orient='index')
    df.index.name = 'x'
    df = df.reset_index()
    df['color'] = get_sample(colors, len(df))

    fig = go.Figure()

    for i, row in df.iterrows():
        # # Add shadow effect
        # fig.add_trace(go.Scatter(
        #     x=[row['x']],
        #     y=[row['y']],
        #     marker=dict(
        #         size=row['impact'] * 6.5,  # Increased bubble size
        #         color='rgba(50, 50, 50, 0.1)'  # Light shadow
        #     ),
        #     mode='markers',
        #     hoverinfo='skip',
        #     showlegend=False
        # ))

        # Add main bubble
        fig.add_trace(go.Scatter(
            x=[row['x']],
            y=[row['y']],
            marker=dict(
                size=row['impact'] * 5,  # Main bubble size
                color=row['color'],
                line=dict(color=freq_color, width=1)
            ),
            mode='markers',
            hovertext=row['hover'],
            hoverinfo='text',
            name=row['name']
        ))

        # Add main bubble
        fig.add_trace(go.Scatter(
            x=[row['x']],
            y=[row['y']],
            marker=dict(
                size=row['impact'] * 4,  # Main bubble size
                color='#fafAfA',
                line=dict(color=freq_color, width=1)
            ),
            mode='markers',
            hovertext=row['hover'],
            hoverinfo='text',
            name=row['name']
        ))

        # Add dotted line connecting bubble to x-axis
        fig.add_trace(go.Scatter(
            x=[row['x'], row['x']],
            y=[0, row['y'] - 2],
            mode='lines',
            line=dict(color='#EFEFEF', width=1, dash='dot'),
            hoverinfo='skip',
            showlegend=False
        ))

        # Add vertical milestone name starting from the zero line
        fig.add_annotation(
            x=row['x'],
            y=.2,
            text=row['text'],
            showarrow=False,
            font=dict(size=12, color=freq_color, family='Arial'),
            textangle=-90,
            align="center",
            xanchor="center",
            yanchor="bottom"
        )

        # # Add label above the bubble
        # fig.add_annotation(
        #     x=row['x'],
        #     y=row['y'] + 2,
        #     text=row['name'],
        #     showarrow=False,
        #     font=dict(size=12, color=freq_color, family='Arial, bold'),
        #     align="center",
        #     xanchor="center",
        #     yanchor="bottom"
        # )

        # Add custom image/icon
        fig.add_layout_image(
            dict(
                source=Image.open(get_image_path(row['icon'])),
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="middle",
                x=row['x'],
                y=row['y'],
                sizex=1.5,
                sizey=1.5,
                sizing="contain",
                opacity=0.8,
                layer="above"
            )
        )

    # Add button-like labels for x-axis
    for i, row in df.iterrows():
        fig.add_annotation(
            x=row['x'],
            y=-1.5,  # Position just below the zero line
            text=str(row['x']),
            showarrow=False,
            font=dict(size=12, color='black', family='Arial'),
            align="center",
            xanchor="center",
            yanchor="middle",
            bgcolor=row['color'],  # Use DataFrame color column
            bordercolor='gray',  # Border color for the button
            borderwidth=1,  # Width of the border
            borderpad=2,  # Padding for rounded corners
            opacity=1
        )

    # Update layout for overall appearance
    fig.update_layout(
        xaxis=dict(
            showline=False,
            tickvals=[],  # Remove default x-axis ticks
            ticktext=[]  # Remove default x-axis text
        ),
        yaxis=dict(
            showline=False,
            showgrid=False,
            zeroline=True,
            zerolinecolor='gray',
            zerolinewidth=1,
            tickvals=[],
            ticktext=[]
        ),
        plot_bgcolor='rgba(255, 255, 255, 1)',  # White background
        paper_bgcolor='rgba(255, 255, 255, 1)',  # White background
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=20),
        height=500,
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)
