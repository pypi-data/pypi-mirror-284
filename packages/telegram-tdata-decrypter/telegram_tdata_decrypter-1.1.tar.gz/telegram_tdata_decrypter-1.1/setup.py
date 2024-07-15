from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="telegram_tdata_decrypter",
    version="1.1",
    description='decrypter tdata to session',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='small_shushu',  # Optional
    install_requires=['tgcrypto']
)
