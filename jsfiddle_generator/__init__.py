#!/usr/bin/env python
import jsfiddle
import os


class JSFiddle:
    """JSFiddle class. attrs: `path`, `css`, `js`, `html`, `name`, `description`, `resources`. methods: `create()`"""
    resources = []
    name = None
    description = None
    css = None
    js = None
    html = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def create(self):
        self.create_css()
        self.create_details()
        self.create_js()
        self.create_html()

    def create_css(self):
        path = os.path.join(os.getcwd(), "demo.css")
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.css if self.css else "")

    def create_details(self):
        path = os.path.join(os.getcwd(), "demo.details")
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        details = dict(
            name=self.name if self.name else os.path.basename(os.getcwd()),
            description=self.description if self.description else "todo",
            resources=self.resources if self.resources else [""]
        )
        if os.path.exists(path):
            data = jsfiddle.details.load()
            details.update(data)
        jsfiddle.details.save(details)

    def create_html(self):
        path = os.path.join(os.getcwd(), "demo.html")
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.html if self.html else "")

    def create_js(self):
        path = os.path.join(os.getcwd(), "demo.js")
        if not os.path.exists(os.getcwd()):
            os.makedirs(os.getcwd())
        if not os.path.exists(path):
            open(path, "w").write(self.js if self.js else "")


# jsfiddle_generator.create()
# python -m jsfiddle_generator .
# find . -name "demo.html" | sed 's/\/[^\/]*$//' | xargs python -m jsfiddle_generator
# find . -name "demo.*" | sed 's/\/[^\/]*$//' | xargs python -m my_jsfiddle.bootstrap
