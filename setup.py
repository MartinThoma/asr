# Core modules
import io
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

config = {
    'name': 'asr',
    'version': '0.1.4',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'packages': ['asr'],
    'scripts': ['bin/asr'],
    # 'package_data': {'asr': ['templates/*', 'misc/*']},
    'url': 'https://github.com/MartinThoma/asr',
    'license': 'MIT',
    'description': 'Automatic Speech Recognition (ASR) tools',
    'long_description': read('README.md'),
    'long_description_content_type': 'text/markdown',
    'install_requires': [
        # "argparse",
        # "theano"
    ],
    'keywords': ['ASR', 'recognition', 'speech'],
    'download_url': 'https://github.com/MartinThoma/asr',
    'classifiers': ['Development Status :: 7 - Inactive',
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
