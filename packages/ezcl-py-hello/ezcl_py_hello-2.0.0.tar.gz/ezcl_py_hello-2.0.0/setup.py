from setuptools import setup, find_packages

setup(
    name='ezcl-py-hello',
    version='2.0.0',
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
