<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/jsfiddle-generator.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-generator/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/jsfiddle-generator.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/jsfiddle-generator.py/actions)

### Installation
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

#### Related
+   [`jsfiddle-build.py` - build `build.html` from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

#### Links
+   [Display fiddle from Gist](https://docs.jsfiddle.net/github-integration/untitled)
+   [Display fiddle from a Github repository](https://docs.jsfiddle.net/github-integration/untitled-1)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>