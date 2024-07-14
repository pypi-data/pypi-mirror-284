from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file

setup(
    name='flask_admin_panel',
    version = "0.1.0",
    url="https://github.com/pranjgit/flask-admin-panel",  # Optional
    
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",        
    ],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords = ["flask","flask-admin","admin-panel","flask-admin-panel", "setuptools", "development"],  # Optional
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),  # Required    
    python_requires=">=3.8, <4",
    include_package_data=True,
    install_requires=[
        "Flask>=3.0.0",
        "Flask-Injector>=0.15.0",
        "Flask-JWT-Extended>=4.6.0",
        "flask-marshmallow>=1.2.0",
        "Flask-Migrate>=4.0.5",
        "flask-restx>=1.3.0",
        "Flask-SQLAlchemy>=3.1.1",
        "Flask-WTF>=1.2.1",
        "WTForms-Alchemy>=0.18.0"
    ],    
    extras_require={  # Optional        
        "test": ["coverage","pytest","pytest-cov"],
    },
    package_data={
        'flask_admin_panel': ['flask_admin_panel/templates/flask_admin_panel/*.html']
    },
    author='Pranjal Gharat',
    author_email='pranjgit@gmail.com',
    description='Simple Admin Panel for Flask',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',    
)
