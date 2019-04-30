import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-codeyaml-plugin',
    version='0.0.16',
    description='A MkDocs plugin that injects the mkdocs.yml extra variables PLUS additional YML files into the markdown template',
    long_description=read('README.md'),
    keywords='mkdocs python markdown extra values PLUS extra yml',
    url='https://github.com/textileio/mkdocs-codeyaml-plugin/',
    author='textile',
    author_email='contact@textile.io',
    license='MIT',
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'mkdocs>=0.17'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'codeyaml = codeyaml.plugin:CodeYamlPlugin'
        ]
    }
)
