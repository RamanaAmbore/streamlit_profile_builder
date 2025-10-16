import streamlit as st

from src.utils import get_image_bin_file, config, profile


# Function to set a PNG image as the page background
def set_png_as_page_bg(png_file, icon=False):
    bin_str = get_image_bin_file(png_file)  # Convert image file to binary string
    page_bg_img = f'''
    <style>
        .appview-container {{
            background-image: url("{bin_str}");
            background-repeat: repeat-y;  # Repeat image vertically
            background-size: cover;  # Make image cover the entire page
            background-position: top;  # Align image to the top
        }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)  # Apply custom styles using Markdown
    return


# Function to render Markdown text with optional styling
def markdown(text, style_tag=True):
    if style_tag:
        text = f'<style>{text}</style>'  # Wrap text in <style> tag for styling
    st.markdown(f'{text}', unsafe_allow_html=True)  # Render styled Markdown


# Wrapper function for streamlit's container element to support function calls within it
def container(*args, **kwargs):
    function = args[0]  # The function to be executed within the container
    args = args[1:]
    if 'key' in kwargs:
        key = kwargs.pop('key')  # Unique key for container
        container = st.container(key=key)
        with container:
            return function(*args, **kwargs)  # Return function inside container

    return function(*args, **kwargs)  # Return function without container


# Function to display a section heading with an optional icon and styling
def write_section_heading(text, portfolio=False):
    icon = config["section_icons"]  # Get icon from config based on section name
    if not portfolio:
        st.subheader(f':{icon[text]}: {text.title()}', anchor=text.title(), divider='rainbow')  # Display section heading
    else:
        text1 = f'Personal Portfolio Projects'
        st.subheader(f':{icon[text]}: {text1.title()}', anchor=text.title(),
                     divider='rainbow')  # Display section heading



# Function to display a subheading with text
def write_subheading(heading, text, key=None):
    st.write(f"**{heading.title()}:** {text}")  # Display heading and text


# Function to display an icon with text and a link, with optional custom HTML tag
def disp_icon_text(icon=None, text=None, link=None, tag=""):
    icon = get_image_bin_file(icon)  # Get the binary string of the icon image
    text = "" if text is None else text
    if tag == "":
        tag = f"<img src='{icon}' class='href_icon'>{text}"  # Format icon with text
    else:
        tag = f"<{tag}><img src='{icon}' class='href_icon'>{text}</{tag}>"  # Use custom HTML tag for text

    if link is None:
        markdown_text = f"""
                <div class='icon_href_text_div'>
                    <span class='href_link'> 
                        {tag}
                    </span>
                </div>
                """
    else:

        markdown_text = f"""
                    <div class='icon_href_text_div'>
                        <span> 
                            <a href="{link}" 
                            class='href_link'><span class='href_text'>{tag}</a>
                        </span>
                    </div>"""

    st.markdown(markdown_text, unsafe_allow_html=True)


# Function to create a horizontal rule (line)
def create_ruler():
    st.markdown('---', unsafe_allow_html=True)  # Render a horizontal rule using Markdown


# Function to display profile information in a container based on the name
def write_container(name):
    profile_section = profile[name]  # Get profile section for the given name
    for key, vals in profile_section.items():
        disp_icon_text(vals['icon'], vals['long label'], vals['link'])  # Display icon and text for each profile item


# Function to display profile information in columns
def write_columns(column_list, name):
    profile_section = profile[name]  # Get profile section for the given name
    profile_keys = list(profile_section.keys())  # List of profile keys
    size = len(profile_keys) - 1  # Total number of profile items
    profile_vals = list(profile_section.values())  # List of profile values

    for idx, col in enumerate(column_list):  # Loop through the columns to display content
        if idx > size: return  # Stop if the column index exceeds the number of profile items
        vals = profile_vals[idx]  # Get the profile values for the current index
        label = vals['label'] if 'label' in vals else profile_keys[idx]  # Use 'label' if it exists
        with col:
            disp_icon_text(vals['icon'], label, vals['link'])  # Display the profile icon, label, and link
