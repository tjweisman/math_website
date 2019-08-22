#!/usr/bin/env python

import sys
import os
import re
import shutil

import markdown
from mako.template import Template
from mako.lookup import TemplateLookup

from ruamel.yaml import YAML

SCRIPT_DIR = "/home/teddy/math/webpage"
TEMPLATE_DIR = "templates"
SITE_DATA = "site_data.yaml"
SITE_DIR = "site"
OUTPUT_DIR = "public_html"

DEFAULT_MARKDOWN_TEMPLATE="markdown_page.html"

HTMLFILE_REGEX = r".+\.html?$"
MDFILE_REGEX = r".+\.md$"

IGNORE_REGEX = ".*~$"

yaml = YAML(typ="safe")

lookup_dirs = TemplateLookup(
    directories=[os.path.join(SCRIPT_DIR, TEMPLATE_DIR),
                 os.path.join(SCRIPT_DIR, SITE_DIR)]
)

def mkoputdir(filename):
    try:
        os.makedirs(os.path.join(SCRIPT_DIR,
                                 OUTPUT_DIR,
                                 os.path.dirname(filename)))
    except os.error:
        pass

def change_ext(filename, new_ext):
    """return a new filename, with the extension changed.
    """
    return re.sub(r"\.\w+$", new_ext, filename)

def ignore_file(filename):
    return re.match(IGNORE_REGEX, filename)

def process_markdown_file(site_data, filename):
    with open(os.path.join(SCRIPT_DIR, SITE_DIR, filename)) as md_file:
        line = md_file.readline()
        title = None
        template_file = DEFAULT_MARKDOWN_TEMPLATE
        while line:
            match = re.match("%\s*(.*)", line)
            if match:
                if not title:
                    title = match.group(1).strip()
                else:
                    template_file = match.group(1).strip()
            else:
                break
            line = md_file.readline()

        html_output = markdown.markdown(md_file.read())

    mkoputdir(filename)

    template = lookup_dirs.get_template(template_file)
    with open(os.path.join(SCRIPT_DIR, OUTPUT_DIR,
                           change_ext(filename, ".html")), "w") as html_file:
        html_file.write(template.render(site_data=site_data,
                                        page_contents=html_output,
                                        page_title=title))


def process_html_file(site_data, filename):
    mkoputdir(filename)
    template = lookup_dirs.get_template(filename)
    with open(os.path.join(SCRIPT_DIR, OUTPUT_DIR, filename), "w") as html_oput:
        html_oput.write(template.render(site_data=site_data))

def process_other_file(site_data, filename):
    mkoputdir(filename)
    shutil.copyfile(os.path.join(SCRIPT_DIR, SITE_DIR, filename),
                    os.path.join(SCRIPT_DIR, OUTPUT_DIR, filename))

def process_file(site_data, filename):
    if ignore_file(filename):
        pass
    elif re.match(HTMLFILE_REGEX, filename):
        process_html_file(site_data, filename)
    elif re.match(MDFILE_REGEX, filename):
        process_markdown_file(site_data, filename)
    else:
        process_other_file(site_data, filename)


def load_site_data():
    with open(os.path.join(SCRIPT_DIR, SITE_DATA), "r") as site_data_file:
        site_data = yaml.load(site_data_file)

    return site_data


def build_site():
    site_data = load_site_data()
    site_files = os.walk(os.path.join(SCRIPT_DIR, SITE_DIR),
                         followlinks=True)

    for dirpath, dirnames, filenames in site_files:
        filedir = os.path.relpath(dirpath, os.path.join(SCRIPT_DIR, SITE_DIR))
        for filename in filenames:
            process_file(site_data, os.path.join(filedir, filename))

def clean_site():
    try:
        shutil.rmtree(os.path.join(SCRIPT_DIR, OUTPUT_DIR))
    except FileNotFoundError:
        pass

    os.mkdir(os.path.join(SCRIPT_DIR, OUTPUT_DIR))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "clean":
            clean_site()
        elif sys.argv[1] == "build":
            build_site()
        else:
            print("Unrecognized command: {}".format(sys.argv[1]))
    else:
        build_site()
