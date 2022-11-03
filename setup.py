from setuptools import setup, find_packages

setup(
    name="auto-reports-sql",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["click", "click-config-file", "jinja2"],
    entry_points="""
    [console_scripts]
    auto-reports-sql=auto_reports_sql:main
    """,
)
