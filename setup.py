import setuptools

#with open('README.md', 'r') as fh:
#   long_description = fh.read()

setuptools.setup(
    name='chip-chip',
    version='0.1.0',
    author='Jake Lehle',
    author_email='jake.lehle@utsa.edu',
    description='End-to-end ChIP-seq data analysis pipeline',
    packages=[
        'cli',
        'snakemake_wrapper',
        'shiny'
    ],
    py_modules=[
        'cli'
    ],
    package_data={
        'snakemake_wrapper': [
            #'annotation/*',
            'scripts/*.R',
            #'submodules/camel/**/*',
            'envs/*.yaml',
            'Snakefile'
        ],
        'shiny': [
            '*.R'
        ],
        'cli': [
            #'annotation_download_links.yaml',
            'optionals.yaml'
        ]
    },
    install_requires=[
        'click',
        'ruamel.yaml',
        'snakemake'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research'
    ],
    entry_points='''
        [console_scripts]
        chip-chip=cli.cli:main
    '''
)
