from setuptools import setup, find_packages

setup(
    name='removeb',  # Replace with your package name
    version='0.1.0',  # Initial release version
    packages=find_packages(),
    description='A package to remove brackets from an array',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pr0ngle',
    author_email='prongle1234@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
