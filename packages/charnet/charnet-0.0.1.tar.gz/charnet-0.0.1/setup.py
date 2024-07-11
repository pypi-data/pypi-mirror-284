from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name='charnet',
    version='0.0.1',
    description='Character interaction temporal graph analysis',
    package_dir={'': 'app'},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MediaCompLab/CharNet',
    author='Media Computing Lab',
    author_email='shu13@gsu.edu',
    license='GPL-3.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas',
        'networkx',
        'numpy',
        'matplotlib',
        'plotly',
        'gravis',
        'pyvis',
    ],
    extras_require={
        'dev': ['pytest>=7.0','twine>=4.0.2']
    },
    python_requires='>=3.6',
)
