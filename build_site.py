#!/usr/bin/env python

import sys
import os
import re
import shutil

from argparse import ArgumentParser

import markdown
from markdown_include.include import MarkdownInclude
from mako.template import Template
from mako.lookup import TemplateLookup

from ruamel.yaml import YAML

SCRIPT_DIR = "/home/teddy/math/web/personal"
SITES_LIST = "sites.yaml"

DEFAULT_SITE = "weisman"

TEMPLATE_DIR = "templates"
SITE_DATA = "site_data.yaml"
SITE_DIR = "site"
OUTPUT_DIR = "public_html"

DEFAULT_MARKDOWN_TEMPLATE="markdown_page.html"

HTMLFILE_REGEX = r".+\.html?$"
MDFILE_REGEX = r".+\.md$"

IGNORE_REGEX = ".*~$"

yaml = YAML(typ="safe")

class SiteBuilder:
    def __init__(self, site_dir):
        self.site_dir = os.path.join(SCRIPT_DIR, site_dir)
        self.load_site_data()
        self.ignore_patterns = [IGNORE_REGEX]

        self.lookup_dirs = TemplateLookup(
            directories=[os.path.join(self.site_dir, TEMPLATE_DIR),
                         os.path.join(self.site_dir, SITE_DIR)],
            input_encoding='utf-8'
        )

        self.markdown_include = MarkdownInclude(
            configs={'base_path':
                     os.path.join(self.site_dir, SITE_DIR)
            }
        )

    def add_ignore_pattern(self, pattern):
        self.ignore_patterns.append(pattern)

    def add_ignores(self, ignores):
        self.ignore_patterns += ignores

    def mkoputdir(self, filename):
        try:
            os.makedirs(os.path.join(self.site_dir,
                                     OUTPUT_DIR,
                                     os.path.dirname(filename)))
        except os.error:
            pass

    def load_site_data(self):
        with open(os.path.join(self.site_dir, SITE_DATA), "r") as site_data_file:
            self.site_data = yaml.load(site_data_file)

    def process_markdown_file(self, filedir, filename):
        title, template_file, html_output = get_mdfile_data(
            os.path.join(self.site_dir, SITE_DIR, filename),
            extensions=[self.markdown_include]
        )

        self.mkoputdir(filename)

        template = self.lookup_dirs.get_template(template_file)
        output_filename = change_ext(filename, ".html")

        page_data = {"title": title,
                     "contents": html_output,
                     "directory":filedir,
                     "filename": output_filename}

        with open(os.path.join(self.site_dir, OUTPUT_DIR,
                               output_filename),
                  "w", encoding='utf-8') as html_file:
            html_file.write(template.render(site_data=self.site_data,
                                            page_data=page_data))

    def process_html_file(self, filename):
        self.mkoputdir(filename)
        template = self.lookup_dirs.get_template(filename)
        with open(os.path.join(self.site_dir, OUTPUT_DIR, filename), "w",
                  encoding='utf-8') as html_oput:
            html_oput.write(template.render(site_data=self.site_data))

    def process_other_file(self, filename):
        self.mkoputdir(filename)
        shutil.copyfile(os.path.join(self.site_dir, SITE_DIR, filename),
                        os.path.join(self.site_dir, OUTPUT_DIR, filename))

    def ignore_file(self, filename):
        for regex in self.ignore_patterns:
            if re.match(regex, filename):
                return True
        return False

    def process_file(self, filedir, filename):
        if self.ignore_file(filename):
            pass
        elif re.match(HTMLFILE_REGEX, filename):
            self.process_html_file(filename)
        elif re.match(MDFILE_REGEX, filename):
            self.process_markdown_file(filedir, filename)
        else:
            self.process_other_file(filename)

    def build_site(self):
        site_files = os.walk(os.path.join(self.site_dir, SITE_DIR),
                             followlinks=True)

        for dirpath, dirnames, filenames in site_files:
            filedir = os.path.relpath(dirpath, os.path.join(self.site_dir, SITE_DIR))
            if filedir == ".":
                filedir = ""
            for filename in filenames:
                self.process_file(filedir, os.path.join(filedir, filename))

    def clean_site(self):
        try:
            shutil.rmtree(os.path.join(self.site_dir, OUTPUT_DIR))
        except FileNotFoundError:
            pass

        os.mkdir(os.path.join(self.site_dir, OUTPUT_DIR))

def get_mdfile_data(abspath, extensions=[]):
    with open(abspath, "r", encoding='utf-8') as md_file:
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

        html_output = markdown.markdown(md_file.read(), extensions=extensions)

    return (title, template_file, html_output)

def change_ext(filename, new_ext):
    """return a new filename, with the extension changed.
    """
    return re.sub(r"\.\w+$", new_ext, filename)

def ignore_file(filename, regex=IGNORE_REGEX):
    return re.match(IGNORE_REGEX, filename)

def load_sites():
    with open(os.path.join(SCRIPT_DIR, SITES_LIST), "r") as sites_list:
        return yaml.load(sites_list)


def build_argument_parser():
    parser = ArgumentParser()

    parser.add_argument("-c", "--clean", action="store_true",
                        help="""Clean the site output rather than rebuilding the site""")

    parser.add_argument("-r", "--rebuild", action="store_true",
                        help="""Clean the site output and then rebuild the site""")

    parser.add_argument("--mkv", action="store_true",
                        help="""don't ignore mkv files when copying""")

    parser.add_argument("--exclude", action="append",
                        help="""regex to exclude when copying files""")

    parser.add_argument("--site", default=DEFAULT_SITE,
                        help="""which site to build/clean""")

    parser.add_argument("-a", "--all", action="store_true",
                        help="""apply action to all sites""")

    return parser

def main():
    parser = build_argument_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.all:
        sites = load_sites()
    else:
        sites = [args.site]

    print(sites)

    for site in sites:
        sitebuilder = SiteBuilder(site)

        if args.exclude:
            sitebuilder.add_ignores(args.exclude)

        if not args.mkv:
            sitebuilder.add_ignore_pattern(r".*\.mkv")

        if args.clean or args.rebuild:
            sitebuilder.clean_site()

        if not args.clean:
            sitebuilder.build_site()

if __name__ == "__main__":
    main()
