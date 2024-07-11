# setup.py

from setuptools import setup, find_packages

setup(
    name='arachnea',
    version='0.0.3',
    packages=find_packages(),
    description='A Python library for efficient array operations using a fluent API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    keywords='array operations, data processing, lightweight, Python library',
    url='https://github.com/yourusername/arachnea',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/Spyder01/arachnea-python',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
