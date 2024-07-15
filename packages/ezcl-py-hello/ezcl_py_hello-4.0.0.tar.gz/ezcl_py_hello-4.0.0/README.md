| Status      | Proposed                                                           |
|-------------|--------------------------------------------------------------------|
| Category    | Library                                                            |
| Team        | [Developer](https://github.com/orgs/easycloudlife/teams/Developer) |
| Authors(s)   | [eazycloudlife](https://github.com/eazycloudlife)                  |
| Created By  | Jul 2024                                                           |
| Modified By | Jul 2024                                                           |
---

## What is this repository for?
- This is the `ezcl hello python library` repository.

Creating a `"Hello, World!"` package in Python is a great way to learn the basics of packaging and distributing Python libraries. Here’s a step-by-step guide to create a simple `"Hello, World!"` package:

## index
- [Step-by-Step Guide](#step-by-step-guide)
    - [1. Set Up Your Project Directory](#1-set-up-your-project-directory)
    - [2. Create the Package Structure](#2-create-the-package-structure)
    - [3. Implement Your "Hello, World!" Function](#3-implement-your-hello-world-function)
    - [4. Create __init__.py](#4-create-initpy)
    - [5. Write setup.py](#5-write-setuppy)
    - [6. Write README.md](#6-write-readmemd)
    - [7. Install Your Package Locally](#7.-install-your-package-locally)
    - [8. Test Your Package](#8-test-your-package)
    - [9. Document Your Library](#9-document-your-library)
    - [10. Publish Your Package (Optional)](#10-publish-your-package-optional)
- [Summary](#summary)
- [Who do I talk to?](#who-do-i-talk-to)
- [Authors](#authors)

### Step-by-Step Guide

#### 1. Set Up Your Project Directory
Create a new directory for your project. Let's name it `ezcl-py-hello`.

```shell
mkdir ezcl-py-hello
cd ezcl-py-hello
```

**[⬆ Back to index](#index)**

#### 2. Create the Package Structure
Inside your `ezcl-py-hello` directory, create the following structure:

```bash
ezcl-py-hello/
└── hello/
    ├── __init__.py
    └── world.py
└── test/
    ├── __init__.py
    └── test_hello.py.py
├── .gitignore
├── LICENSE
├── README.md
├── setup.py
├── requirements.txt
├── run.py
├── setup.py
```

- `hello/__init__.py`: This file will initialize your package.
- `hello/world.py`: This file will contain your "Hello, World!" function.

**[⬆ Back to index](#index)**

#### 3. Implement Your "Hello, World!" Function
Open `hello/world.py` and write the following Python code:

```python
def hello(name):
    """
    In return, Hello, name!.

    """
    return f"Hello, {name}!"

def hello_world():
    """
    In return, Hello, World!.

    """
    return "Hello, World!"

def hi(name):
    """
    In return, Hello, name!.

    """
    return f"Hi, {name}"

def hi_world():
    """
    In return, Hi, World!.

    """
    return "Hi, World!"

```

**[⬆ Back to index](#index)**

#### 4. Create __init__.py

In `hello/__init__.py`, include the following:

```python
from .world import hello_world
```
This imports the hello_world function from world.py into your package.

**[⬆ Back to index](#index)**

#### 5. Write setup.py
Create setup.py in your project root directory (hello_world_package) with the following content:

```python
from setuptools import setup, find_packages

setup(
    name='ezcl-py-hello',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],  # No dependencies for this simple package
    entry_points={
        'console_scripts': [
            'hello-world = hello.world:hello_world'
        ]
    },
    author='Eazy Cloud Life',
    author_email='wazycloudlife@email.com',
    description='A simple "Hello, World!" package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eazycloudlife/ezcl-py-hello',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    extras_require={},
    python_requires=">=3.12.4",
)

```

Replace `Your Name`, `your@email.com`, and `https://github.com/yourusername/hello_world_package` with your information.

**[⬆ Back to index](#index)**

#### 6. Write README.md
Create `README.md` and write a brief description of your package.

**[⬆ Back to index](#index)**

#### 7. Install Your Package Locally
To `test` your package locally, run the following command in the hello_world_package directory:

```bash
pip install .
```
This will install your package in the current Python environment.

**[⬆ Back to index](#index)**

#### 8. Test Your Package
Create a Python script to test your package. For example, create `test_hello.py`:

```python
from hello import (
    hello,
    hello_world,
    hi,
    hi_world
)

def test_hello(name):
    assert hello(name) == f"Hello, {name}!"
    print("Test passed!")

def test_hello_world():
    assert hello_world() == "Hello, World!"
    print("Test passed!")

def test_hi(name):
    assert hi(name) == f"Hi, {name}"
    print("Test passed!")

def test_hi_world():
    assert hi_world() == "Hi, World!"
    print("Test passed!")

if __name__ == "__main__":
    name = "Eazy Cloud Life"
    
    test_hello(name)
    test_hello_world()
    test_hi(name)
    test_hi_world()

```

Run python `test_hello.py` to verify that your package works correctly.

**[⬆ Back to index](#index)**

#### 9. Document Your Library

Use docstrings ("""...""") to document each function, class, and module.
Consider generating documentation using tools like Sphinx.

**[⬆ Back to index](#index)**

#### 10. Publish Your Package (Optional)

If you want to share your package with others, consider publishing it on `PyPI`. You will need to [`create an account on PyPI`](https://pypi.org/account/register/) and follow their guidelines for uploading packages.

- Package your library using setuptools:

    ```python
    python setup.py sdist bdist_wheel
    ```
- Create the PyPI token to Upload your package to PyPI.
    - **Log in to PyPI**:
        - Go to [PyPI](https://pypi.org/manage/account/) and log in with your account.
    - **Create a Token**:
        - Click on your `username` in the top right corner and select `"Account settings."`
        - Scroll down to the `"API tokens"` section and click on `"Add API token."`
        - Give your token a name (e.g., "my-package-upload-token").
        - Choose the `scope` of the token. You can either create a token with `"Entire account"` scope or "Project: `your-project-name`" scope. For most cases, it's better to use the project scope for security reasons.
        - Click `"Add token."`
        - Click Copy button to Copy token.
- Upload your package to PyPI or another package repository:

    ```python
    twine upload dist/*
    ```
    - Once you've passed the token, it will now appear when you press Enter.

        ![Diagram](images/upload-package.png)
- Go to [PyPI](https://pypi.org/manage/projects/) and check you `projects  / package`.
        
    ![Diagram](images/package.png)

**[⬆ Back to index](#index)**

### Summary
Creating a `"Hello, World!"` package involves defining a simple function, organizing your code into a package structure, writing a `setup.py` file for packaging, and optionally testing and publishing your package. This exercise provides a solid foundation for understanding Python packaging and distribution.

**[⬆ Back to index](#index)**

### Who do I talk to?
- [Developer Team](https://github.com/orgs/easycloudlife/teams/Developer) or [eazycloudlife](https://github.com/eazycloudlife) **[⬆ Back to index](#index)**

### Authors
A repository is maintained by [eazycloudlife](https://github.com/eazycloudlife) with help from [these awesome contributors](https://github.com/eazycloudlife/ezcl-py-hello/graphs/contributors). **[⬆ Back to index](#index)**
