from streamlit_option_menu import option_menu


def get_option_menu():
    selected = option_menu("", ['Summary', 'Experience', 'Skills', 'Certifications', 'Projects', 'Hobbies'],
                           icons=['house', 'person', 'gear', 'trophy', 'folder', 'joystick'], menu_icon="cast",
                           default_index=0,
                           styles={
                               "container": {"padding": "0!important", "background-color": "#2c4653"},
                               "icon": {"color": "white", "font-size": "20px", "fond-weight": "bold"},
                               "nav-link": {"font-size": "16px", "text-align": "left", "color":"white", "margin": "0px",
                                            "--hover-color": "#616365"},
                               "nav-link-selected": {"background-color": "#e6873a"}}
                           )
