#!/usr/bin/env python3

import os
import argparse

import yaml
from jinja2 import Environment, Template, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def render_template(template_path, data):
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(os.path.join(THIS_DIR, 'templates')), trim_blocks=True)
    j2_template = j2_env.get_template(template_path)
    return j2_template.render(**data)


def load_config_data(data_path):
  with open(data_path, "r") as data_descriptor:
    return yaml.load(data_descriptor, Loader=yaml.FullLoader)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Template render for OCS configs files. If no output file specified the script will print to STDOUT.'
    )
    parser.add_argument('--template-path', '-t', help='Template path from template folder', required=True)
    parser.add_argument('--data-path', '-d', help='Data path, relative or absolute path to yaml file', required=True)
    parser.add_argument('--output', '-o', help='Path to output file where to print rendered template')
    args = parser.parse_args()

    data = load_config_data(args.data_path)
    template = render_template(args.template_path, data)

    if args.output is None:
        print(template)
    else:
        with open(args.output, "w") as fd:
            fd.write(template)
