from setuptools import setup, find_packages

with open(r"assessment\readme.md" , "r") as file:
    long_description = file.read()

with open(r"LICENSE.txt", "r") as file:
    licence = file.read()

setup(
    name = "dcg-extensionmigrationassistant",
    version = "1.0.1", 
    author = "DataCloudGaze Consulting",
    author_email = "contact@datacloudgaze.com",
    description = "Detect Lock-in Extension wrapper introduce as part of conversion tool",
    long_description = long_description,
    long_description_content_type ="text/markdown",
    licence = licence,
    url = "https://github.com/dcgadmin/extensionmigrationassistant.git",
    package_dir={"": "."},  
    packages=find_packages(),
    python_requires = ">=3.0",
    install_requires = [
                        "Jinja2",
                        "matplotlib",
                        "numpy",
                        "pandas",
                        "psycopg2-binary",
                        "SQLAlchemy"
                        ],

    entry_points = {"console_scripts": ["extension-assessment=assessment.assessment:main"]},   
    package_data={'': ["*.csv", "*.html"]},                                    
    include_package_data = True,
    classifiers = [
                    "Programming Language :: Python :: 3",
                    "Development Status :: 5 - Production/Stable",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                    "Environment :: Console"
                    ],

)
