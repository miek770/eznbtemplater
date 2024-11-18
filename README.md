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

A fully functional [LaTeX environnement](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex) must be available to [nbconvert](https://nbconvert.readthedocs.io/en/latest/) on your system; instructions vary. Please refer these two links if your [LaTeX](https://www.latex-project.org/) conversion fails.

## Usage

The package provides 2 templater functions: `render_nb` and `render_pdf`. Both work the same way; a [Jupyter Notebook](https://jupyter.org/) template must be provided (`.ipynb` file or `nbformat.NotebookNode` object), the output path must be specified and keywords (identified as `{{keyword}}` in the template) can be provided with their type to update the template.

Here is `render_pdf`'s function definition:

```python
def render_pdf(
    *,
    output_path: Path,
    template_nb: Optional[nbformat.NotebookNode] = None,
    template_path: Optional[Path] = None,
    **kwargs,
):
```

Any number of keyword arguments can be provided to match and replace `{{keyword}}` fields in the [Jupyter Notebook](https://jupyter.org/) template (`.ipynb` file or `nbformat.NotebookNode` object). If desired, a keyword argument with the same name plus `_cell_type` can be provided to change the resulting notebook cell type, e.g.: to `markdown`.

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

![example](https://raw.githubusercontent.com/miek770/eznbtemplater/refs/heads/main/media/test_pandas_pdf.png)

This is the `test_nb_programatically()` test from [tests/test_nb_programatically.py](tests/test_nb_programatically.py); it works with a notebook template created with [nbformat](https://pypi.org/project/nbformat/) inspired by [this example](https://gist.github.com/fperez/9716279) instead of a notebook file:

```python
from eznbtemplater.eznbtemplater import render_nb
import nbformat as nbf
from pathlib import Path


def test_nb_programatically() -> None:
    nb: nbf.NotebookNode = nbf.v4.new_notebook()
    nb["cells"] = [
        nbf.v4.new_raw_cell(r"\renewcommand{\contentsname}{Table of Contents}"),
        nbf.v4.new_raw_cell(r"\tableofcontents"),
        nbf.v4.new_markdown_cell("# Introduction"),
        nbf.v4.new_markdown_cell("{{introduction}}"),
    ]

    output_path: Path = Path("tests/test_nb_programatically.ipynb")

    introduction: str = "This is a ***test***, don't mind me."
    render_nb(
        template_nb=nb,
        output_path=output_path,
        introduction=introduction,
    )
    assert output_path.exists()
```

See [tests/test_renderers.py](tests/test_renderers.py) for a few additional examples.

## Contributing

Contributions are welcome; please:

- Use [uv](https://github.com/astral-sh/uv).
- Run `uv sync` to install the development environment.
- Run `uv run pre-commit install` to active the pre-commit hooks, including [black](https://github.com/psf/black).
- Ensure [pytest](https://docs.pytest.org/en/stable/) runs without failures with `make tests`.
- Be nice.

The source code is hosted at [https://github.com/miek770/eznbtemplater](https://github.com/miek770/eznbtemplater).

## License

`eznbtemplater` is licensed under the MIT License. See [LICENSE](LICENSE) file for details.
