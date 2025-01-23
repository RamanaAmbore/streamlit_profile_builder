import functools
import logging
import random

import yaml
from PIL import Image
import base64
from io import BytesIO


class CustomDict(dict):
    def __getitem__(self, key):
        for k in self.keys():
            if k.endswith(key):
                return super().__getitem__(k)

        return None


with open('data/profile_data.yaml', 'r', errors='ignore') as file:
    profile = yaml.safe_load(file)
    projects = CustomDict(profile['projects'])
    education = CustomDict(profile['education'])
    certifications = CustomDict(profile['certifications'])
    skills = CustomDict(profile['skills'])
    contact = CustomDict(profile['contact'])
    social = CustomDict(profile['social'])
    milestones = CustomDict(profile['milestones'])

with open("src/frontend/custom_styles.css") as css:
    css_style = css.read()

with open('src/setup/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    colors = config['dark_colors']
    dark_colors = config['dark_colors']
    sidebar_icons = config['sidebar_icons']
    section_icons = config['section_icons']
    freq_color = config['freq_color']


def get_image_path(file, icon=True):
    return f'static/icons/{file}' if icon else f'static/images/{file}'


def del_seq(parm_text):
    if '.' in parm_text[1:2]: parm_text = parm_text.split('.', 1)[1]
    return parm_text


def get_image_bin_file(file, icon=True):
    img = Image.open(get_image_path(file, icon))
    format = file[-3:].upper()

    # Encode the image as base64
    buffered = BytesIO()
    img.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    url = f'data:image/{format.lower()};base64,{img_str}'
    return url


def debug_wrapper(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logging.debug(f'{function.__name__} started')
        result = function(*args, **kwargs)
        logging.debug(f'{function.__name__} ended')
        return result

    return wrapper


def get_sample(lst, size):
    return random.sample(lst, size) if len(lst) > size else random.choices(lst, size)


def get_config(name):
    section = config[name]
    return list(section.keys()), list(section.values())


def get_profile(name):
    section = profile[name]
    return list(section.keys()), list(section.values())


def capitalize(text):
    return text if text.isupper() else text.title()


def get_labels(name, label='label'):
    section = profile[name]
    return [capitalize(vals[label] if label in vals else key) for key, vals in section.items()]


def get_darker_color(hex_color, factor=0.5):
    """
    Darkens a hex RGB color by a given factor.

    :param hex_color: The original color in hex format (e.g., "#RRGGBB").
    :param factor: A float between 0 and 1. The lower the factor, the darker the color.
    :return: A darkened color in hex format.
    """
    if not (0 <= factor <= 1):
        raise ValueError("Factor must be between 0 and 1")

    # Remove the hash (#) if present
    hex_color = hex_color.lstrip('#')

    # Convert the hex color to RGB components
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)

    # Apply the darkening factor
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)

    # Ensure values are within 0-255 range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Convert back to hex and return
    return f"#{r:02x}{g:02x}{b:02x}"


def get_darker_colors(hex_color_list, factor=0.75):
    return [get_darker_color(color, factor) for color in hex_color_list]
