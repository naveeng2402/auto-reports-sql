from setuptools import setup, find_packages

with open("readme.md") as f:
    readme = f.read()

setup(
    name="auto-reports-sql",
    version="1.0.5",
    description="This tool automates SQL Reports generation.",
    author="Naveen G",
    url="https://github.com/naveeng2402/auto-reports-sql.git",
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    keywords=[
        "sql",
        "automation",
        "data science",
        "data analytics",
        "sqlite",
        "mysql",
        "postgres",
    ],
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        "click",
        "click-config-file",
        "jsonschema",
        "jinja2",
        "colorama",
        "psycopg2-binary",
        "mysql-connector-python",
    ],
    entry_points="""
    [console_scripts]
    auto-reports-sql=auto_reports_sql:main
    """,
)
