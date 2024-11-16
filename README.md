# eznbtemplater

As in ***easy notebook templater***.

Generates PDF and [Jupyter Notebook](https://jupyter.org/) files from a notebook template (`.ipynb` file).

I made this small and simple library to facilitate the creation of professionnal looking reports and calculation notes programatically, without having to learn extensive templating engines or mess with more [LaTeX](https://www.latex-project.org/) than desired. My previous attempts of accomplishing this goal involved using existing packages that did not yield satisfactory results for [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). This one does!

## Installation

Install the package from [PyPI](https://pypi.org/) with [pip](https://pypi.org/project/pip/) using:

```
pip install eznbtemplater
```

### Additional Requirements

A fully functional [LaTeX environnement](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/latex_envs/README.html) must be available to [nbconvert](https://nbconvert.readthedocs.io/en/latest/) on your system; instructions vary. Please refer these two links if your [LaTeX](https://www.latex-project.org/) conversion fails.

## Usage

The package provides 2 templater functions: `render_nb` and `render_pdf`. Both work the same way; a [Jupyter Notebook](https://jupyter.org/) template must be provided (`.ipynb` file), the output path must be specified and keywords (identified as `{{keyword}}` in the template) can be provided with their type to update the template.

Here is `render_pdf`'s function definition:

```python
def render_pdf(
    *,
    template_path: Path,
    output_path: Path,
    **kwargs,
):
```

Any number of keyword arguments can be provided to match and replace `{{keyword}}` fields in the [Jupyter Notebook](https://jupyter.org/) template (`.ipynb` file). If desired, a keyword argument with the same name plus `_cell_type` can be provided to change the resulting notebook cell type, e.g.: to `markdown`.

### Example

This is the `test_pandas_pdf()` test from [tests/test_renderers.py](tests/test_renderers.py); it replaces the `{{calculations}}` keyword with a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to generate a PDF report.

```python
import pandas as pd
from pathlib import Path
from eznbtemplater import render_pdf

template_path: Path = Path("eznbtemplater/templates/calculation_note.ipynb")

output_path: Path = Path("tests/test_pandas.pdf")

headers = ["Food", "Color", "Type"]
data: list = [
    ["Apple", "Red", "Fruit"],
    ["Tomato", "Red", "Fruit"],
    ["Mushroom", "Grey", "Fungi"],
    ["Pie", "Beige", "Desert"],
]
df: pd.DataFrame = pd.DataFrame(
    data=data,
    columns=headers,
).set_index("Food")

render_pdf(
    template_path=template_path,
    output_path=output_path,
    calculations=df.to_markdown(),
    calculations_cell_type="markdown",
)
```

Here is the PDF result (margins were cropped for this picture, and the `{{introduction}}`, `{{inputs}}`, `{{conclusion}}` and `{{references}}` appear without their curly braces because they weren't replaced in the example):

![](media/test_pandas_pdf.png)

See [tests/test_renderers.py](tests/test_renderers.py) for a few additional examples.

## Contributing

Contributions are welcome; please:

- Use [uv](https://github.com/astral-sh/uv).
- Run `uv sync` to install the development environment.
- Run `uv run pre-commit install` to active the pre-commit hooks, including [black](https://github.com/psf/black).
- Ensure [pytest](https://docs.pytest.org/en/stable/) runs without failures with `make tests`.
- Be nice.

## License

`eznbtemplater` is licensed under the MIT License. See [LICENSE](LICENSE) file for details.
