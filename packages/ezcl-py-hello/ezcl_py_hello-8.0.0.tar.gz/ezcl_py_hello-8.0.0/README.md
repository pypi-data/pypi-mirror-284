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
- [How is the Python library created?](#how-is-the-python-library-created)
- [How to install?](#how-to-install)
- [How to uninstall?](#how-to-uninstall)
- [How to upgrade?](#how-to-upgrade)
- [Examples of How To Use](#examples-of-how-to-use)
    - [Importing the package](#importing-the-package)
    - [Using the package](#using-the-package)
- [Summary](#summary)
- [Who do I talk to?](#who-do-i-talk-to)
- [Authors](#authors)


### How is the Python library created?

- [Github README.md](https://github.com/eazycloudlife/ezcl-py-hello)

- [Medium](https://medium.com/@eazycloudlife/how-is-the-python-library-created-b6a55bdf3d80)


### How to install?

```bash
pip install ezcl-py-hello
```
![Diagram](images/install.png)

### How to uninstall?

```bash
pip uninstall ezcl-py-hello
```
![Diagram](images/uninstall.png)

### How to upgrade?

```bash
pip install --upgrade ezcl-py-hello
```
![Diagram](images/upgrade.png)

### Examples of How To Use

#### Importing the package

```python
from hello import (
    hello,
    hello_world,
    hi,
    hi_world,
    version
)
```

#### Using the package

```python
def say_hello(name):
    return hello(name)

def say_hello_world():
    return hello_world()

def say_hi(name):
    return hi(name)

def say_hi_world():
    return hi_world()

def say_version():
    return version()

if __name__ == "__main__":
    name = "Eazy Cloud Life"

    print(say_hello(name))
    print(say_hello_world())
    print(say_hi(name))
    print(say_hi_world())
    print(say_version())
    print(hello.__version__)

```

**[⬆ Back to index](#index)**

### Summary
Creating a `"Hello, World!"` package involves defining a simple function, organizing your code into a package structure, writing a `setup.py` file for packaging, and optionally testing and publishing your package. This exercise provides a solid foundation for understanding Python packaging and distribution.

**[⬆ Back to index](#index)**

### Who do I talk to?
- [Developer Team](https://github.com/orgs/easycloudlife/teams/Developer) or [eazycloudlife](https://github.com/eazycloudlife) **[⬆ Back to index](#index)**

### Authors
A repository is maintained by [eazycloudlife](https://github.com/eazycloudlife) with help from [these awesome contributors](https://github.com/eazycloudlife/ezcl-py-hello/graphs/contributors). **[⬆ Back to index](#index)**
