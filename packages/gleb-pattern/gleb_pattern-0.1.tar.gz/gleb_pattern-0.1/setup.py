from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gleb_pattern',
    version='0.1',
    description='Comic library for a friend',
    packages=['gleb_pattern'],
    author_email='nn@elros.ru',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)