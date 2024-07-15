# hello/__init__.py

def get_version():
    # Logic to retrieve version dynamically, e.g., from a file or environment variable
    return "7.0.0"

__version__ = get_version()

from .world import hello, hello_world, hi, hi_world, version