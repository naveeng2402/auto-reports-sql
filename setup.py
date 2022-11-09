from setuptools import setup, find_packages

setup(
    name="auto-reports-sql",
    version="0.0.1",
    long_description="This tool automates SQL Reports generation",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "click-config-file", "jsonschema", "jinja2", "colorama"],
    entry_points="""
    [console_scripts]
    auto-reports-sql=auto_reports_sql:main
    """,
)
