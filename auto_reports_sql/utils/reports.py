import os
from typing import Iterator
from jinja2 import Template
import pkgutil


def check_and_rename(file: str, rendered_html: str, add=0):
    original_file = file
    if add != 0:
        split = file.split(".")
        part_1 = split[0] + "_" + str(add)
        file = ".".join([part_1, split[1]])
    if not os.path.isfile(file):
        with open(file, "w+") as f:
            f.write(rendered_html)
    else:
        check_and_rename(original_file, rendered_html, add=add + 1)


def generate_report(
    data: Iterator[
        tuple[
            str, tuple[tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]], ...]
        ],
    ],
) -> None:

    template_content = pkgutil.get_data(__name__, "../templates/light.html.j2").decode()
    title = os.getenv("report_title")

    template = Template(template_content)
    rendered_html = template.render(data=data, title=title)

    reports_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(reports_dir):
        os.mkdir(reports_dir)

    # with open(os.path.join(reports_dir, f"{title}.html"), "w+") as f:
    #     f.write(rendered_html)
    check_and_rename(os.path.join(reports_dir, f"{title}.html"), rendered_html)
