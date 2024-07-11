from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipdd',  
    version='3.0',  
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'ipdd=ipdd.downloader:download',
        ],
    },
    author='豬嘎嘎',
    author_email='piggaga.company@gmail.com',
    description='Download images from Google search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://piggaga.github.io/piggaga',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
