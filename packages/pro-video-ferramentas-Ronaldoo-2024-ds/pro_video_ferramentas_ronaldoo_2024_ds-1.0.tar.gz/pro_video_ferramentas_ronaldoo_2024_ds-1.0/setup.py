from setuptools import setup, find_packages
from pathlib import Path
with open('README.md', 'r') as arq:
    readme = arq.read()


setup(
    name='pro-video-ferramentas-Ronaldoo-2024-ds',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de video',
    long_description=Path('README.md').read_text(),
    author='Ronaldo',
    author_email='Ronaldo@gmail.com',
    keywords=['Camera','Video','Processamento'],
    packages=find_packages()
)