from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# from src.custom_css import about_me_styles
from src.utils.constants import about_me_summary, about_me_name, about_me_designation
from src.utils.custom_css import about_me_styles
from src.utils.utils import set_png_as_page_bg, get_base64_of_bin_file, show_image

# from src.utils.utils import set_png_as_page_bg


# Profile picture and About Me section
profile_picture = "assets/images/saad.png"
about_me_bg_color = "#3c4b67"
about_me_text_color = "#333333"

favicon = Image.open("assets/images/favicon.ico")

if __name__ == '__main__':
    st.set_page_config(page_title="Ramana Ambore(Rambo)'s Profile", page_icon=favicon, layout="wide")
    # set_png_as_page_bg('assets/images/test.png')
    st.markdown(about_me_styles, unsafe_allow_html=True)
    with st.sidebar:

        selected = option_menu("", ['Summary', 'Experience', 'Skills', 'Certifications', 'Projects', 'Hobbies'],
                               icons=['house', 'person', 'gear', 'trophy', 'folder', 'joystick'], menu_icon="cast", default_index=0,
                               styles={
                                   "container": {"padding": "0!important", "background-color": "#2c4653"},
                                   "icon": {"color": "white", "font-size": "20px", "fond-weight": "bold"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                                "--hover-color": "#616365"},
                                   "nav-link-selected": {"background-color": "#e6873a"}}
                               )


    col1, div, col2 = st.columns([1.5,.1,10])
    with col1:
         st.image('assets/images/ramana_photo1.png',clamp=True, use_container_width=True)
    with col2:
        st.header(f'{about_me_name}')
        # st.header(about_me_name)
        st.markdown(f'<h4 style="color:#f87408;font-weight:bold;padding-top:0rem;letter-spacing:0px">{about_me_designation}</h4>', unsafe_allow_html=True)
        # st.write(about_me_designation)
        st.write(about_me_summary)

