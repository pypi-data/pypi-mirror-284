from setuptools import setup, find_packages

setup(
    name='TurboImpute',
    version='0.1.0',
    author='Valentine Mwangi',
    author_email='valentine@afterwork.ai',
    description='A library for handling missing values in datasets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/valentinemwangi/TurboImpute',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ],
    python_requires='>=3.6',
)