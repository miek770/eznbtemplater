from nbconvert.exporters import LatexExporter
import nbformat
from pathlib import Path
from typing import Any


import tempfile
from pathlib import Path
from typing import Any
import nbformat
from nbconvert import PDFExporter


def render_nb(
    *,
    template_path: Path,
    output_path: Path,
    **kwargs,
):

    # Replace {{keys}} in the template
    nb: Any = _process_template(
        template_path=template_path,
        **kwargs,
    )

    # Write the modified notebook to a temporary file
    with open(output_path, "w", encoding="utf-8") as output_file:
        nbformat.write(nb, output_file)


def render_pdf(
    *,
    template_path: Path,
    output_path: Path,
    **kwargs,
):

    # Replace {{keys}} in the template
    nb: Any = _process_template(
        template_path=template_path,
        **kwargs,
    )

    # Write the modified notebook to a transition file
    transit_filename: Path = output_path.with_suffix(".ipynb")
    with open(transit_filename, mode="w", encoding="utf-8") as output_file:
        nbformat.write(nb, output_file)

    # Use nbconvert to convert the temporary notebook to a PDF
    pdf_exporter = PDFExporter()
    pdf_exporter.exclude_input = True  # Example option to exclude input cells
    pdf_body, resources = pdf_exporter.from_filename(transit_filename.as_posix())

    # Save the generated PDF to the output path
    with open(output_path, "wb") as output_file:
        output_file.write(pdf_body)


def _process_template(
    template_path: Path,
    **kwargs,
) -> Any:

    # Read the template notebook
    with open(template_path, "r", encoding="utf-8") as template_file:
        nb: Any = nbformat.read(template_file, as_version=4)

    # Replace placeholders in the notebook
    for cell in nb.cells:
        for key in kwargs.keys():
            if f"{{{{{key}}}}}" in cell.source:
                cell.source = cell.source.replace(
                    f"{{{{{key}}}}}",
                    kwargs[key],
                )
                if f"{key}_cell_type" in kwargs.keys():
                    cell.cell_type = kwargs[f"{key}_cell_type"]

    return nb
