# Import necessary modules and components
import pandas as pd
import streamlit as st
from plotly import graph_objects as go
from streamlit_scroll_navigation import scroll_navbar

# Import custom components and functions from src directory
from src.components import container, write_section_heading, create_ruler, write_colums, write_container, \
    disp_icon_text
from src.utils import profile, get_image_path, get_selected_colors, get_image_bin_file, freq_color, get_config, \
    get_profile, \
    colors, get_labels, capitalize, get_darker_colors, get_darker_color, pdf_resume


# Function to generate the sidebar section
def generate_sidebar_section():
    # Fetch configuration for sidebar icons
    key_list, val_list = get_config('sidebar_icons')
    key_list = [x.title() for x in key_list]

    with st.sidebar:
        # Display the sidebar menu using Streamlit option menu
        scroll_navbar(
            key_list,
            anchor_labels=None,
            anchor_icons=val_list,
            override_styles={
                "navbarButtonBase": {
                    "backgroundColor": "#2f4550",  # Set a custom button background color
                    "color": "#ffffff"  # Set custom text color

                }, "navbarButtonHover": {
                    "backgroundColor": "#3da4ab",  # Set a custom hover color for the buttons
                },
                "navbarButtonActive": {
                    "backgroundColor": "#e76801",  # Change the navigation bar background color
                },
                "navigationBarBase": {
                    "backgroundColor": "#2f4550",  # Change the navigation bar background color
                }

            }

        )


# Function to generate the profile section
def generate_profile_section():
    # Display profile name and designation
    st.markdown(f"<div id='summary_section'></div>", unsafe_allow_html=True)
    container(st.header, f"{profile['name']}, {profile['name suffix']}", anchor="Summary", key='profile_name')

    container(st.write, f"#### {profile['designation']}", key='profile_designation')

    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        # Display profile photo
        container(st.image, get_image_path('profile_photo.png'), clamp=True,
                  use_container_width=True, key='profile_photo')
    with col2:
        # Display profile details
        container(st.write, profile['profile'], key='profile')
        # Add a button to download the resume as a PDF
        container(st.download_button, label=":arrow_down: pdf", type='tertiary',
                  data=pdf_resume,
                  file_name=f"{profile['name'].lower()}.pdf",
                  mime='application/octet-stream', key="pdf_download")


# Function to generate the contact and social media section
def generate_contact_social_section():
    create_ruler()  # Add a horizontal ruler

    # Contact section
    section_name = 'contact'
    with st.container(key=section_name):
        width_cols = [1, .05, 1, 0.05, 1, .05, 1]
        col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
        write_colums([col1, col2, col3, col4], section_name)

    # Social media section
    section_name = 'social'
    with st.container(key=section_name):
        width_cols = [1, .05, 1, 0.05, 1, .05, 1]
        col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
        write_colums([col1, col2, col3, col4], section_name)


# Function to generate the experience summary section
def generate_experience_summary_section():
    section_name = 'experience summary'
    write_section_heading(section_name, key=section_name)  # Add section heading
    generate_milestone_section()  # Generate milestone section

    val_list = profile[section_name]
    with st.container(key='summary_points'):
        # Display each experience summary point as a list item
        for line in val_list:
            st.write(f"- {line}")


# Function to generate the skills section
def generate_skills_section():
    section_name = 'skills'
    key_list, val_list = get_profile(section_name)

    write_section_heading(section_name, key=section_name)  # Add section heading

    # Prepare data for skills bar chart
    categories = get_labels(section_name)
    icon_paths = [val['icon'] for val in val_list]
    ratings = [val['level'] for val in val_list]
    hover = [val['long label'] for val in val_list]
    select_colors = get_selected_colors(colors, len(ratings))
    border_colors = get_darker_colors(select_colors)

    img_base64 = [get_image_bin_file(icon) for icon in icon_paths]

    # Create bar chart using Plotly
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=ratings,
        text='',
        textposition='inside',
        insidetextanchor='start',
        marker=dict(
            color=select_colors,  # Base color
            line=dict(color=border_colors, width=1)  # Shadow effect with darker border
        ),
        hovertemplate='%{customdata}<extra></extra>',
        customdata=hover
    ))

    for i, category in enumerate(categories):
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
        xaxis_title=dict(text="Skills", font=dict(color=freq_color, size=14)),
        yaxis_title=dict(text="Proficiency", font=dict(color=freq_color, size=14)),
        xaxis=dict(tickangle=0, showticklabels=False, ),
        yaxis=dict(range=[0, 5]),
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent overall background
        margin=dict(t=20, b=20),
        showlegend=False
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


def generate_hobbie_section():
    # Generate the "Hobbies" section of the profile
    section_name = 'hobbies'  # Section identifier
    section = profile[section_name]  # Load hobbies data from the profile
    write_section_heading(section_name, key=section_name)  # Add a section heading
    st.write(section['summary'])  # Display summary of hobbies

    # Define column layout for images
    width_education = [6, .05, 2, 2]

    # Create columns for displaying images of hobbies
    col1, _, col2, _ = container(st.columns, width_education,
                                 vertical_alignment='center', key='hobbie_container')
    with col1:
        st.image(get_image_path('drone.png'))  # Display the first hobby image

    with col2:
        st.image(get_image_path('raspberry.png'))  # Display the second hobby image

    with st.expander("Additional Information..."):
        st.write(section['additional information'])  # Display additional hobby details


def generate_education_section():
    # Generate the "Education" section of the profile
    section_name = 'education'  # Section identifier
    key_list, val_list = get_profile(section_name)  # Retrieve profile data for education
    write_section_heading(section_name, key=section_name)  # Add a section heading

    # Define column layout
    width_education = [5, .05, 1]

    # Create columns for education details and pie chart
    education_col, _, education_pie_chart_col = container(st.columns, width_education,
                                                          vertical_alignment='center', key='education_container')
    with education_col:
        write_container('education')  # Display education details

    with education_pie_chart_col:
        labels = get_labels(section_name, 'short label')  # Get labels for education pie chart
        values = [val['duration'] for val in val_list]  # Extract duration values
        hover = [(val['hover'] if 'hover' in val else val['long label']).replace(',', '<br>') for val in val_list]
        select_colors = get_selected_colors(colors, len(labels))  # Select colors for the chart
        border_colors = get_darker_colors(select_colors)  # Darken colors for border

        # Create a pie chart to visualize education data
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color=border_colors, width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
                   pull=[0.03] * len(labels))])

        # Update chart layout for customization
        fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
            showlegend=False,
            margin=dict(t=0, b=0),
            height=150
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)


def generate_certification_section():
    # Generate the "Certifications" section of the profile
    section_name = 'certifications'  # Section identifier
    key_list, val_list = get_profile(section_name)  # Retrieve certification data
    write_section_heading(section_name, key=section_name)  # Add section heading

    # Define column layout
    width_education = [5, .05, 1]

    # Create columns for certifications details and pie chart
    col, _, pie_chart_col = container(st.columns, width_education,
                                      vertical_alignment='center', key='certification_container')
    with col:
        write_container('certifications')  # Display certification details

    with pie_chart_col:
        labels = get_labels(section_name, 'short label')  # Get labels for the pie chart
        values = [val['duration'] for val in val_list]  # Extract duration values
        hover = [(val['hover'] if 'hover' in val else val['long label']).replace(',', '<br>') for val in val_list]
        select_colors = get_selected_colors(colors, len(labels))  # Select colors for the chart
        border_colors = get_darker_colors(select_colors)  # Darken colors for border

        # Create a pie chart for certifications
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color=border_colors, width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
                   pull=[0.03] * len(labels))])

        # Update chart layout for customization
        fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
            showlegend=False,
            margin=dict(t=0, b=0),
            height=150
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

# Function to generate the employment section
def generate_employment_section():
    section_name = 'employment'
    key_list, val_list = get_profile('projects')  # Retrieve profile data for the projects section
    write_section_heading(section_name, key=section_name)  # Add section heading for employment

    width_education = [5, .05, 1]  # Define column widths for layout

    # Create columns for employment section layout
    col, _, pie_chart_col = container(st.columns, width_education,
                                      vertical_alignment='center', key=f'{section_name}_data')
    with col:
        write_container('projects')  # Write project details in the left column

    with pie_chart_col:
        labels = get_labels('projects')  # Retrieve labels for pie chart
        values = [val['duration'] for val in val_list]  # Get project durations for pie chart values
        hover = [(val['hover'] if 'hover' in val else val['long label']).replace(',', '<br>') for val in val_list]  # Prepare hover text for the pie chart
        select_colors = get_selected_colors(colors, len(labels))  # Get selected colors for pie chart
        border_colors = get_darker_colors(select_colors)  # Get darker colors for pie chart borders

        # Create pie chart using Plotly
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color=border_colors, width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
                   pull=[0.03] * len(labels))])  # Add slight pull-out effect for all slices

        # Update pie chart layout for custom appearance
        fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
            showlegend=False,  # Hide legend
            margin=dict(t=0, b=0),  # Adjust margins
            height=150  # Set height for pie chart
        )

        # Display the pie chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)


# Function to generate the portfolio section
def generate_portfolio_section():
    section_name = 'portfolio'
    write_section_heading(section_name, key=section_name)  # Add section heading for portfolio
    section = profile[section_name]  # Retrieve portfolio section data

    # Iterate over each portfolio item
    for key, vals in section.items():
        container = st.container(key=key)  # Create a container for each portfolio item
        with container:
            col1, _, col2 = st.columns([10, 0.01, 10])  # Define column layout for portfolio item
            with col1:
                disp_icon_text(vals['icon'], key, vals['link'], 'h5')  # Display project icon and link
            with col2:
                disp_icon_text('git_small.png', '', vals['github'])  # Display GitHub icon and link

            col1, _, col2 = st.columns([10, 0.01, 5])  # Define column layout for project details
            with col1:
                st.write(vals['summary'])  # Display project summary
                st.write(f"Technology: {vals['technology']}")  # Display technologies used
            with col2:
                st.image(get_image_path(vals['image']))  # Display project image

            with st.expander(f"Additional Information..."):
                st.write(vals['additional information'])  # Display additional information about the project


# Function to generate the project section
def generate_project_section():
    section_name = 'projects'
    write_section_heading(section_name, key=section_name)  # Add section heading for projects
    section = profile[section_name]  # Retrieve projects section data

    # Iterate over each project
    for key, vals in section.items():
        container = st.container(key=f"{section_name}_{key}")  # Create a container for each project
        with container:
            label = capitalize(vals['label'] if 'label' in vals else key)  # Capitalize the project label
            disp_icon_text(vals['icon'], label, vals['link'], 'H5')  # Display project icon and link

            # Iterate over clients for the project
            for key1, vals1 in vals['clients'].items():
                for key2, vals2 in vals1.items():
                    # Display client details
                    st.write(
                        f"**{key2}, {key1}, {vals2['role']}, {vals2['start']} - {vals2['end']}**")
                    st.write(f"{vals2['summary']}")  # Display project summary
                    st.write(f"Technology: {vals2['technology']}")  # Display technologies used
                    with st.expander(f"Additional Information..."):
                        st.write(vals2['additional information'])  # Display additional project information


# Function to generate the milestone section
def generate_milestone_section():
    section_name = 'milestones'
    section = profile[section_name]  # Retrieve milestones section data
    df = pd.DataFrame.from_dict(section, orient='index')  # Convert milestone data to DataFrame
    df.index.name = 'x'  # Name index column
    df = df.reset_index()  # Reset index to prepare for visualization
    df['color'] = get_selected_colors(colors, len(df))  # Assign colors for milestones

    fig = go.Figure()

    # Iterate over each milestone and create annotations
    for i in range(len(df)):
        row = df.iloc[i]
        color = row['color']
        border_color = get_darker_color(color, .25)

        # Add annotation for milestone
        fig.add_annotation(
            x=i * .5,
            y=0.5,
            text=f"<span style='line-height:11px;background-color:{color};font-weight:bold;'> {str(row['x'])}  </span>" f"<span style='line-height:11px;'>{row['milestone']}</span>",
            showarrow=False,
            font=dict(size=13, color="black"),
            align="center",
            xanchor="center",
            yanchor="bottom",
            textangle=-90,
            bgcolor=row['color'],
            bordercolor=border_color,
            borderwidth=1,
            borderpad=5,
            opacity=1,
            hovertext=row['long label'],
        )

    # Update layout for overall appearance
    fig.update_layout(
        xaxis=dict(showline=False, tickvals=[], ticktext=[]),  # Hide x-axis details
        yaxis=dict(range=[0, 5], showline=False, showgrid=False, zeroline=True, zerolinecolor='#efefef', zerolinewidth=1, tickvals=[], ticktext=[]),  # Format y-axis
        plot_bgcolor='rgba(255, 255, 255, 0)',  # Set plot background
        paper_bgcolor='rgba(255, 255, 255, 0)',  # Set paper background
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        height=200,
    )

    # Display the chart in Streamlit
    milestone_container = st.container(key=section_name)
    with milestone_container:
        st.plotly_chart(fig)  # Display milestone chart
