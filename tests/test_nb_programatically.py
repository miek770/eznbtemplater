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
