from setuptools import setup, find_packages

setup(
    name='colorate_console',
    version='0.2.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'colorize=colorate_console.colorizer:main'
        ],
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Colorateur de textes dans un terminal",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0',
)
