try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'asr',
    'version': '0.1.2',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'packages': ['asr'],
    'scripts': ['bin/asr'],
    # 'package_data': {'asr': ['templates/*', 'misc/*']},
    'url': 'https://github.com/MartinThoma/asr',
    'license': 'MIT',
    'description': 'Automatic Speech Recognition (ASR) tools',
    'long_description': """Tools for ASR""",
    'install_requires': [
        # "argparse",
        # "theano",
        # "nose",
        # "natsort",
        # "PyYAML",
        # "matplotlib",
        # "shapely"
    ],
    'keywords': ['ASR', 'recognition', 'speech'],
    'download_url': 'https://github.com/MartinThoma/asr',
    'classifiers': ['Development Status :: 1 - Planning',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: MIT License',
                    'Natural Language :: English',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Topic :: Scientific/Engineering :: Artificial Intelligence',
                    'Topic :: Software Development',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
