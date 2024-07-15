from setuptools import setup, find_packages

setup(
    name='stubbingmytoe',
    version='0.1.0',
    author='macturner',
    author_email='mac@stubbingmytoe.ca',
    description='A package that includes various tools, including a color extractor',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/macturnerr2002/stubbingmytoe',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'scikit-learn',
        'tqdm',
        'matplotlib',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'color_extractor=stubbingmytoe.color_extractor.extractor:proccessImage',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
