from setuptools import setup, find_packages

setup(
    name='turtle-fr',
    version='1.0.0',
    requires=["tkinter", "PIL"],
    packages=find_packages(),
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Version simplifée en français du module turtle",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    python_requires='>=3.0',
)
