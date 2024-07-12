# Comando para subir o arquivo para Pypi
#  -> twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# Link para README (License)
# https://opensource.org/license/MIT?_gl=1*1h97ohi*_ga*OTIxMjU1Mjk4LjE3MDM2OTE1Mjk.*_ga_37GXT4VGQK*MTcyMDY2MDUwOS4zMi4xLjE3MjA2NjA4ODQuMC4wLjA.

from setuptools import setup,find_packages
from pathlib import Path

setup(
    name='Arquivo-teste-Leonardo-2024-ds',
    version='1.0',
    description='Este pacote tem a finalidade de teste',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    author='Leonardo',
    author_email='leosousa@',
    keywords=['camera','video','Como_publicar_projeto_Pypi'],
    packages=find_packages()


)