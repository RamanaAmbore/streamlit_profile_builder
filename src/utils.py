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
    career = CustomDict(profile['career'])
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
    colors = config['colors']
    dark_colors =  config['dark_colors']
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


def get_config (name):
    section = config[name]
    return list(section.keys()), list(section.values())


def get_profile (name):
    section = profile[name]
    return list(section.keys()), list(section.values())
