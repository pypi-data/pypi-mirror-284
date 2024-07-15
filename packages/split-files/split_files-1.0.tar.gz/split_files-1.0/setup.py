from setuptools import setup, find_packages

setup(
    name='split-files',
    version='1.0',
    author='Lutfifakee',
    author_email='lutfifakee@proton.me',
    description='Utility for splitting files into smaller parts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/X-Projetion/split-files',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            '0xsplit = 0xsplit:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/X-Projetion/split-files/issues',
        'Source': 'https://github.com/X-Projetion/split-files',
        'Wiki': 'https://github.com/X-Projetion/split-files/wiki',
        'GitHub Statistics': 'https://github.com/X-Projetion/split-files/graphs',
    },
)
