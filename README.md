# resvg-py

`resvg-py` provides a Python interface to the [`resvg`](https://github.com/RazrFalcon/resvg/) library, an open-source Rust-based SVG rendering library that can be used to convert SVG images to various other formats such as PNG, PDF, and SVGZ.

The purpose of `resvg-py` is to provide a convenient way to use `resvg` from within Python code, without the need for external dependencies.  By using `resvg-py`, developers can incorporate SVG rendering functionality directly into their Python applications, making it easier to work with SVG images and to create high-quality, scalable graphics for their projects.

With `resvg-py`, developers can:

* Load SVG files and render them to various output formats
* Control the output size, resolution, and quality of the rendered images
* Work with SVG images directly within their Python code, without the need for external tools or libraries

Overall, `resvg-py` provides a simple and powerful way to work with SVG images in Python, and can be a useful tool for developers who need to work with vector graphics in their projects.


# Usage

```python
from pathlib import Path

import resvg_py
from PIL import Image

options = resvg_py.SVGOptions()
r = resvg_py.Resvg(options)

with Path("resources/examples/svg/octocat.svg").open("r") as f:
    rendered = r.render(f.read(), 400, 400)
    array = rendered.as_array()
    im = Image.fromarray(array)
    im.save("image.png")

```

# Options

The `Options` class within the `resvg-py` library is responsible for providing customization and configuration options for rendering SVG files.  This class contains properties that define different aspects of the rendering process, such as dimensions, background color, and language. The following documentation will cover each property within the `Options` class, their purpose, and the allowed range of values.

## Properties

|Name|Purpose|Type|Allowed Values|Example|
|:----|:----|:----|:----|:----|
|width|Defines the width of the output image in pixels|Integer|Positive integers (1 and above)|`options.width = 300`|
|height|Defines the height of the output image in pixels|Integer|Positive integers (1 and above)|`options.height = 200`|
|fit_to|Controls how the SVG should be scaled to fit the output|String or Tuple|"original", ("width", value), ("height", value), ("zoom", factor)|`options.fit_to = ("width", 300)`|
|background|Sets the background color of the output image|String or None|6 or 8-digit hex color codes or `None`|`options.background = "#FFAABB"`|
|dpi|Specifies the DPI value used for rendering|Float|Positive float values (greater than 0)|`options.dpi = 96.0`|
|languages|Sets the list of languages for `systemLanguage` attribute|List of strings|Valid [BCP 47](https://tools.ietf.org/html/bcp47) language codes|`options.languages = ["en", "fr", "es"]`|
|shape_rendering|Controls the rendering mode for shapes|String|optimizeSpeed", "crispEdges", "geometricPrecision|`options.shape_rendering = "optimizeSpeed"`|
|text_rendering|Controls the rendering mode for text|String|optimizeSpeed", "optimizeLegibility", "geometricPrecision|`options.text_rendering = "optimizeLegibility"`|
|image_rendering|Controls the rendering mode for images|String|optimizeQuality", "optimizeSpeed", "pixelated|`options.image_rendering = "optimizeQuality"`|
|skip_system_fonts|Skip loading system fonts when rendering text|Boolean|`True` or `False`|`options.skip_system_fonts = True`|
|font_size|Specifies the default font size for text elements|Float|Positive float values (greater than 0)|`options.font_size = 14.0`|
|font_family|Specifies the default font family for text elements|String|Valid font family names|`options.font_family = "Arial"`|
|font_path|Path to a custom font file|String|Valid file path|`options.font_path = "path/to/font.ttf"`|


## Example Usage

```python
from resvg import Options, render_from_file

options = Options()
options.width = 300
options.height = 200
options.background = "#FFAABB"
options.dpi = 96.0
options.languages = ["en", "fr", "es"]
options.shape_rendering = "optimizeSpeed"
options.text_rendering = "optimizeLegibility"
options.image_rendering = "optimizeQuality"

output_image = render_from_file("input.svg", options)
```


# How To Build

## Install Rust, Set up Python Dev Requirements

**Windows**

```sh
choco install rust
```

**Set up Virtual Environemt**

```sh
python -m venv venv
.\venv\Scripts\Activate.bat
```

**Install Maturin and Pytest**

```sh
pip install -r requirements-dev.txt
```

## Build Python Wheel

```sh
maturin develop
```

## Run Tests

```sh
pytest
```

To update the snapshots:

```sh
pytest --snapshot-update
```
