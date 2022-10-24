import os

from jinja2 import Template


def generate_report(
    title: str,
    data: tuple[tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]], ...],
) -> None:

    with open(
        os.path.join(os.getenv("TEMPLATES_PATH"), "report_template.html.j2")
    ) as template_file:
        template_content = template_file.read()

    template = Template(template_content)
    rendered_html = template.render(data=data, title=title)

    reports_dir = os.getenv("REPORT_PATH")
    if not os.path.exists(reports_dir):
        os.mkdir(reports_dir)

    check_and_rename(os.path.join(reports_dir, f"{title}.html"), rendered_html)


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
