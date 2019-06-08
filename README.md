<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/jsfiddle-generator.svg?longCache=True)](https://pypi.org/project/jsfiddle-generator/)
[![](https://img.shields.io/pypi/v/jsfiddle-generator.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-generator/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/jsfiddle-generator.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/jsfiddle-generator.py/)

#### Installation
```bash
$ [sudo] pip install jsfiddle-generator
```

#### How it works
[jsfiddle github repo files](https://docs.jsfiddle.net/github-integration/untitled-1):
```
.
├── demo.html
├── demo.css
├── demo.js
├── demo.details
```

[jsfiddle github gist files](https://docs.jsfiddle.net/github-integration/untitled):
```
.
├── fiddle.html
├── fiddle.css
├── fiddle.js
├── fiddle.manifest
```

#### Classes
class|`__doc__`
-|-
`jsfiddle_generator.JSFiddle` |attrs: `path`, `css`, `js`, `html`, `name`, `description`, `resources`. methods: `create()`
`jsfiddle_generator.JSFiddleGist` |github gist files generator
`jsfiddle_generator.JSFiddleRepo` |github repo files generator

#### Executable modules
usage|`__doc__`
-|-
`python -m jsfiddle_generator.gist path ...` |generate jsfiddle gist files: `fiddle.css`, `fiddle.js`, `fiddle.html`, `fiddle.manifest`
`python -m jsfiddle_generator.repo path ...` |generate jsfiddle repo files: `demo.css`, `demo.js`, `demo.html`, `demo.details`

#### Examples
create `demo.css`, `demo.js`, `demo.details` in every dir with `demo.html`:
```bash
$ find . -name "demo.html" -exec python -m jsfiddle_generator.repo {} \;
```

---
create jsfiddle repo files in every empty dir:

`find . -not -path '*/\.*' -type d -links 2 -exec python -m jsfiddle_generator.repo {} \;`

---
paths with spaces:

OS|speed|command
-|-|-
any|slow|`find ... -exec python -m jsfiddle_generator.repo {} \;`
Linux|fast|`find ... -print0 \| xargs -d '\n' python -m jsfiddle_generator.repo`
macOS|fast|`find ... -print0 \| xargs -0 python -m jsfiddle_generator.repo`

#### Related projects
+   [`jsfiddle-build.py` - build `build.html` from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

#### Links
+   [Display fiddle from Gist](https://docs.jsfiddle.net/github-integration/untitled)
+   [Display fiddle from a Github repository](https://docs.jsfiddle.net/github-integration/untitled-1)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>