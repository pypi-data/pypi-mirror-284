from setuptools import setup

setup(
    name='treezor',
    version='0.1.0',
    requires=['bigtree'],
    entry_points={
        'console_scripts': [
            'tree=tree:main'
        ],
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Permet de lister les dossiers d'un répertoire",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.0',
)
