from setuptools import setup, find_packages

setup(
    name='pythonejs',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='jay',
    author_email='pjay32547@gmail.com',
    description='A simple EJS-like template engine for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/calteen/pythonejs',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
