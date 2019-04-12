#!/usr/bin/env python
import os
import public
import yaml


@public.add
class JSFiddle:
    """attrs: `path`, `css`, `js`, `html`, `name`, `description`, `resources`. methods: `create()`"""
    prefix = None
    resources = []
    name = None
    description = None
    css = None
    js = None
    html = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def create_css(self):
        path = os.path.join(os.getcwd(), "%s.css" % self.prefix)
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.css if self.css else "")

    def create_html(self):
        path = os.path.join(os.getcwd(), "%s.html" % self.prefix)
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.html if self.html else "")

    def create_js(self):
        path = os.path.join(os.getcwd(), "%s.js" % self.prefix)
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.js if self.js else "")


@public.add
class JSFiddleRepo(JSFiddle):
    """github repo files generator"""
    prefix = "demo"

    def create(self):
        self.create_css()
        self.create_details()
        self.create_js()
        self.create_html()

    def create_details(self):
        path = os.path.join(os.getcwd(), "demo.details")
        data = dict(
            name=self.name if self.name else os.path.basename(os.getcwd()),
            description=self.description if self.description else "_",
            resources=self.resources if self.resources else [""]
        )
        if os.path.exists(path):
            data.update(yaml.load(open(path, 'r')))
        yaml.dump(data, open(path, 'w'), default_flow_style=False)


@public.add
class JSFiddleGist(JSFiddle):
    """github gist files generator"""
    prefix = "fiddle"

    def create(self):
        self.create_css()
        self.create_manifest()
        self.create_js()
        self.create_html()

    def create_manifest(self):
        path = os.path.join(os.getcwd(), "fiddle.manifest")
        data = dict(
            name=self.name if self.name else os.path.basename(os.getcwd()),
            description=self.description if self.description else "_",
            resources=self.resources if self.resources else [""],
            normalize_css="no",
            wrap="b",
            panel_js=1,
            panel_css=1
        )
        if os.path.exists(path):
            data.update(yaml.load(open(path, 'r')))
        yaml.dump(data, open(path, 'w'), default_flow_style=False)
