import pandas as pd
from pathlib import Path
from eznbtemplater import render_nb


def test_markdown_nb() -> None:
    template_path: Path = Path("eznbtemplater/templates/calculation_note.ipynb")
    assert template_path.exists()

    output_path: Path = Path("tests/test_markdown_nb.ipynb")

    introduction: str = "This is a ***test***, don't mind me."
    render_nb(
        template_path=template_path,
        output_path=output_path,
        introduction=introduction,
        introduction_cell_type="markdown",
    )
    assert output_path.exists()
