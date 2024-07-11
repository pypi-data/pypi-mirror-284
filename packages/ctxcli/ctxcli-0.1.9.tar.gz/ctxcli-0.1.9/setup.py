from setuptools import setup, find_packages

with open("README.rst", encoding="UTF-8") as f:
    readme = f.read()
    setup(
        name="ctxcli",
        version="0.1.9",
        description="CLI Tools for Amdocs ConnectX",
        long_description=readme,
        long_description_content_type="text/x-rst",
        author="Amdocs ConnectX",
        author_email="roey@benamotz.com",
        packages=find_packages("src"),
        package_dir={"": "src"},
        install_requires=[
            'rich',
            'requests',
            'configparser',
            'pathlib',
            'pandas',
            'openpyxl',
            'tqdm',
            'cachetools',
            'inquirer',
        ],
        entry_points={
            "console_scripts": ["ctxcli=cxcli.cli:main"],
        },
    )
