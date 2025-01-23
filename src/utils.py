import base64
import functools
import logging
import random
from io import BytesIO

import streamlit
import yaml
from PIL import Image


class CustomDict(dict):
    """
    A custom dictionary class that allows partial key matching based on suffix.
    """

    def __getitem__(self, key):
        """
        Get an item from the dictionary where the key ends with the specified suffix.

        :param key: The suffix of the key to match.
        :return: The value associated with the matched key, or None if no match is found.
        """
        for k in self.keys():
            if k.endswith(key):
                return super().__getitem__(k)

        return None


# Load profile data from a YAML file
with open('data/profile_data.yaml', 'r', errors='ignore') as file:
    profile = yaml.safe_load(file)
    projects = CustomDict(profile['projects'])
    education = CustomDict(profile['education'])
    certifications = CustomDict(profile['certifications'])
    skills = CustomDict(profile['skills'])
    contact = CustomDict(profile['contact'])
    social = CustomDict(profile['social'])
    milestones = CustomDict(profile['milestones'])

# Load custom CSS styles for the frontend
with open("src/frontend/custom_styles.css") as css:
    css_style = css.read()

# Load configuration data from another YAML file
with open('src/setup/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    colors = config['dark_colors']
    dark_colors = config['dark_colors']
    sidebar_icons = config['sidebar_icons']
    section_icons = config['section_icons']
    freq_color = config['freq_color']

# Read a PDF file into memory
with open("static/resume.pdf", "rb") as pdf_file:
    pdf_resume = pdf_file.read()


def get_image_path(file):
    """
    Get the file path of an image in the static directory.

    :param file: The filename of the image.
    :return: The full path to the image.
    """
    return f'static/{file}'


@streamlit.cache_resource
def get_image_bin_file(file):
    """
    Converts an image file to a base64-encoded URL.

    :param file: The filename of the image.
    :return: A base64-encoded data URL for the image.
    """
    img = Image.open(get_image_path(file))
    format = file[-3:].upper()

    # Encode the image as base64
    buffered = BytesIO()
    img.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    url = f'data:image/{format.lower()};base64,{img_str}'
    return url


def debug_wrapper(function):
    """
    A decorator for debugging the start and end of function calls.

    :param function: The function to wrap with debugging logs.
    :return: The wrapped function.
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logging.debug(f'{function.__name__} started')
        result = function(*args, **kwargs)
        logging.debug(f'{function.__name__} ended')
        return result

    return wrapper


def get_sample(lst, size):
    """
    Get a random sample or duplicate items if the list is too small.

    :param lst: The list to sample from.
    :param size: The number of items to sample.
    :return: A list of sampled items.
    """
    return random.sample(lst, size) if len(lst) > size else random.choices(lst, size)


def get_config(name):
    """
    Retrieve configuration data by section name.

    :param name: The name of the configuration section.
    :return: A tuple of keys and values from the section.
    """
    section = config[name]
    return list(section.keys()), list(section.values())


def get_profile(name):
    """
    Retrieve profile data by section name.

    :param name: The name of the profile section.
    :return: A tuple of keys and values from the section.
    """
    section = profile[name]
    return list(section.keys()), list(section.values())


def capitalize(text):
    """
    Capitalize the text unless it already contains uppercase characters.

    :param text: The text to capitalize.
    :return: The capitalized text.
    """
    return text if any([x.isupper() for x in text]) else text.title()


def get_labels(name, label='label'):
    """
    Retrieve labels from profile data, capitalizing where necessary.

    :param name: The name of the profile section.
    :param label: The key to use for labels in the section.
    :return: A list of labels.
    """
    section = profile[name]
    return [capitalize(vals[label] if label in vals else key) for key, vals in section.items()]


def get_darker_color(hex_color, factor=0.5):
    """
    Darken a hex RGB color by a specified factor.

    :param hex_color: The original color in hex format (e.g., "#RRGGBB").
    :param factor: A float between 0 and 1. The lower the factor, the darker the color.
    :return: A darkened color in hex format.
    """
    if not (0 <= factor <= 1):
        raise ValueError("Factor must be between 0 and 1")

    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)

    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)

    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return f"#{r:02x}{g:02x}{b:02x}"


def get_darker_colors(hex_color_list, factor=0.75):
    """
    Apply darkening to a list of hex colors.

    :param hex_color_list: A list of hex color codes.
    :param factor: A float between 0 and 1 for the darkening factor.
    :return: A list of darkened colors.
    """
    return [get_darker_color(color, factor) for color in hex_color_list]
