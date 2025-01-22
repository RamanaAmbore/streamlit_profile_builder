import pandas as pd
import streamlit as st
from plotly import graph_objects as go
from streamlit_option_menu import option_menu


from src.components.components import container, write_subheading, create_ruler, write_colums, write_container, \
    disp_icon_text, disp_icon_text_new
from src.utils import profile, get_image_path, get_sample, colors, get_image_bin_file, freq_color, contact, \
    social, education, config, get_config, get_profile, colors, dark_colors, del_seq


def generate_sidebar_section():
    key_list, val_list = get_config('sidebar_icons')
    key_list = [x.title() for x in key_list]
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


def generate_profile_section():
    container(st.header, f'{profile['name']}, {profile['name_suffix']}', key='profile_name')
    # st.header(about_me_name)
    container(st.write, f'#### {profile['designation']}', key='profile_designation')
    col1, _, col2 = st.columns([2, .1, 10])
    with col1:
        container(st.image, get_image_path('profile_photo.png', False), clamp=True,
                  use_container_width=True, key='profile_photo')
    with col2:
        container(st.write, profile['profile'], key='profile')


def generate_contact_social_section():
    create_ruler()
    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], 'contact')

    width_cols = [1, .05, 1, 0.05, 1, .05, 1]
    col1, _, col2, _, col3, _, col4 = st.columns(width_cols, vertical_alignment='center')
    write_colums([col1, col2, col3, col4], 'social')


def generate_summary_section():
    section_name = 'experience summary'
    write_subheading(section_name, key=section_name)
    generate_milestone_section()
    val_list = profile[section_name]
    point_container = st.container(key='summary_points')
    with point_container:
        for line in val_list:
            st.write(f"- {line}")


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


def generate_hobbie_section():
    section_name = 'hobbies'
    write_subheading(section_name, key=section_name)
    st.write(profile[section_name])

    width_education = [6, .05, 2, 2]

    col1, _, col2, _ = container(st.columns, width_education,
                                 vertical_alignment='center', key='hobbie_container')
    with col1:
        st.image(get_image_path('drone.png', icon=False))

    with col2:
        st.image(get_image_path('raspberry.png', icon=False))


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
        hover = [(val['hover'] if 'hover' in val else val['description']).replace(',','<br>') for val in val_list]
        select_colors = get_sample(colors, len(labels))

        # Create pie chart
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color="gray", width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
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
        hover = [(val['hover'] if 'hover' in val else val['description']).replace(',','<br>') for val in val_list]
        select_colors = get_sample(colors, len(labels))

        # Create pie chart
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color="gray", width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
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
        write_container(section_name)

    with pie_chart_col:
        labels = [val['name'] for val in val_list]
        values = [val['duration'] for val in val_list]
        hover = [(val['hover'] if 'hover' in val else val['description']).replace(',','<br>') for val in val_list]
        select_colors = get_sample(colors, len(labels))

        # Create pie chart
        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   values=values,
                   marker=dict(colors=select_colors, line=dict(color="gray", width=1)),
                   textinfo='label', insidetextorientation='radial',
                   textposition='inside',
                   hovertemplate='%{customdata}<extra></extra>',
                   customdata=hover,
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

def generate_portfolio_section():
    section_name = 'portfolio'
    # key_list, val_list = get_profile(section_name)
    write_subheading(section_name, key=section_name)
    profile_section = profile[section_name]
    for key, vals in profile_section.items():
        container = st.container(key=del_seq(key))
        with container:
            disp_icon_text_new(vals['icon'], key, vals['link'],'h5')
            for key1, val1 in vals.items():
                if key1 not in ['icon', 'link']:
                    st.write(f"**{key1}**: {val1}")
            with st.expander(f"Description"):
                st.write(vals['Description'])

def generate_project_section():
    section_name = 'projects'
    # key_list, val_list = get_profile(section_name)
    write_subheading(section_name, key=section_name)
    profile_section = profile[section_name]
    for key, vals in profile_section.items():
        container = st.container(key=f"{section_name}_{del_seq(key)}")
        with container:
            st.markdown(f"**{vals['name']}**")
            for key1, vals1 in vals['clients'].items():
                st.write(key1)
                for key2, vals2 in vals1.items():
                    st.write(f"Project: {key2}, Role: {vals2['role']}, {vals2['start']}-{vals2['end']}")
                    st.write(f"Skills: {vals2['skills']}")
                    st.write(f"Summary: {vals2['summary']}")
                    with st.expander(f"Description"):
                        st.write(vals2['description'])



def generate_milestone_section():
    section = profile['milestones']
    df = pd.DataFrame.from_dict(section, orient='index')
    df.index.name = 'x'
    df = df.reset_index()
    df['color'] = get_sample(colors, len(df))

    fig = go.Figure()

    # Iterate over each milestone in the DataFrame
    for i in range(len(df)):
        row = df.iloc[i]
        color = row['color']
        # Add combined annotation above the zero line with vertical orientation and hover effect
        fig.add_annotation(
            x=i*.5,
            y=0.5,  # Position above the zero line, adjust this for vertical padding

            text=f"<span style='line-height:11px;background-color:{color};font-weight:bold;'> {str(row['x'])}  </span><span style='line-height:11px;'>{row['name']}</span>",  # Combine name and year
            showarrow=False,
            font=dict(size=13, color="black"),
            align="center",
            xanchor="center",
            yanchor="bottom",
            textangle=-90,  # Vertical text orientation
            bgcolor=row['color'],  # Background color for the milestone name
            bordercolor='gray',  # Border color for the annotation
            borderwidth=1,  # Width of the border
            borderpad=5,  # Padding for rounded corners
            opacity=1,
            hovertext=row['description'],  # Hover text for annotation
        )

        # Add combined annotation above the zero line with vertical orientation and hover effect
        fig.add_annotation(
            x=i * .5,
            y=1.55,  # Position above the zero line, adjust this for vertical padding

            text=f"</span><span style='line-height:11px;'>{row['name']}</span>",
            # Combine name and year
            showarrow=False,
            font=dict(size=13, color="black"),
            align="center",
            xanchor="center",
            yanchor="bottom",
            textangle=-90,  # Vertical text orientation
            bgcolor='white',  # Background color for the milestone name
            bordercolor='lightgray',  # Border color for the annotation
            borderwidth=1,  # Width of the border
            borderpad=5,  # Padding for rounded corners
            opacity=1,
            hovertext=row['description'],  # Hover text for annotation
        )

    # Update layout for overall appearance with increased right margin
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
            zerolinecolor='#efefef',
            zerolinewidth=1,
            tickvals=[],
            ticktext=[]
        ),
        plot_bgcolor='rgba(255, 255, 255, 0)',  # White background
        paper_bgcolor='rgba(255, 255, 255, 0)',  # White background
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),  # Increased right margin
        height=200,
    )

    # Display the chart in Streamlit
    milestone_container = st.container(key='milestones')
    with milestone_container:
        st.plotly_chart(fig)
