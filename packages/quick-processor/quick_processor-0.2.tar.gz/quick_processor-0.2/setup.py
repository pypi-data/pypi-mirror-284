from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='quick_processor',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'nltk==3.8.1',
        'contractions==0.1.73',
        'beautifulsoup4==4.12.3',
        'emoji==2.12.1',
        'pyspellchecker==0.8.1',
        'textsearch==0.0.24',
        'click==8.1.7',
        'colorama==0.4.6',
        'joblib==1.4.2',
        'tqdm==4.66.4',
        'regex==2024.5.15',
        'soupsieve==2.5',
        'typing-extensions==4.12.2',
        'anyascii==0.3.2',
        'pyahocorasick==2.1.0'
    ],
    long_description=description,
    long_description_content_type='text/markdown',
)
