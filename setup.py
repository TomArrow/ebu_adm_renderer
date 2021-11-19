from setuptools import setup, find_packages

setup(
    name='da-ear',
    description='EBU ADM Renderer (distance aware)',
    version='0.01',

    url='https://github.com/ebu/ebu_adm_renderer',

    author='EBU',
    author_email='ear-admin@list.ebu.ch',
    license='BSD-3-Clause-Clear',

    long_description=open('README.md').read() + '\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',

    install_requires=[
        'numpy~=1.14',
        'scipy~=1.0',
        'attrs~=19.3',
        'ruamel.yaml~=0.15',
        'lxml~=4.4',
        'six~=1.11',
        'multipledispatch~=0.5',
    ],

    extras_require={
        'test': [
            'pytest>=3.5.1, < 6.0.0',
            'pytest-datafiles~=2.0',
            'pytest-cov~=2.5',
            'soundfile~=0.10',
        ],
        'dev': [
            'flake8~=3.5',
            'flake8-print~=3.1',
            'flake8-string-format~=0.2',
        ],
    },

    packages=find_packages(),

    package_data={
        "da_ear.test": ["data/*.yaml", "data/*.wav"],
        "da_ear.core": ["data/*.yaml", "data/*.dat"],
        "da_ear.core.test": ["data/psp_pvs/*.npz"],
        "da_ear.core.objectbased.test": ["data/gain_calc_pvs/*"],
        "da_ear.fileio.adm": ["data/*.xml"],
        "da_ear.fileio.adm.test": ["test_adm_files/*.xml"],
        "da_ear.fileio.bw64.test": ["test_wav_files/*.wav"],
    },

    entry_points={
        'console_scripts': [
            'da-ear-render = da_ear.cmdline.render_file:main',
            'da-ear-utils = da_ear.cmdline.utils:main'
        ]
    },
)
