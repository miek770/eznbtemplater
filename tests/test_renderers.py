import pandas as pd
from pathlib import Path
from eznbtemplater.eznbtemplater import render_nb, render_pdf


def test_markdown_pdf() -> None:
    template_path: Path = Path("eznbtemplater/templates/calculation_note.ipynb")
    assert template_path.exists()

    output_path: Path = Path("tests/test_markdown_nb.pdf")

    introduction: str = "This is a ***test***, don't mind me."
    render_pdf(
        template_path=template_path,
        output_path=output_path,
        introduction=introduction,
        introduction_cell_type="markdown",
    )
    assert output_path.exists()


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


def test_latex_pdf() -> None:
    template_path: Path = Path("eznbtemplater/templates/calculation_note.ipynb")
    assert template_path.exists()

    output_path: Path = Path("tests/test_latex_nb.pdf")

    introduction: str = r"This is a test, don't mind me\footnote{Hey there!}."
    render_pdf(
        template_path=template_path,
        output_path=output_path,
        introduction=introduction,
        introduction_cell_type="raw",
    )
    assert output_path.exists()


def test_pandas_pdf() -> None:
    template_path: Path = Path("eznbtemplater/templates/calculation_note.ipynb")
    assert template_path.exists()

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
    assert output_path.exists()
